from django.shortcuts import render
import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import Http404
from datetime import datetime
from .models import User, Slot


def index(request):
    return render(request, "meetup/index.html")


def home(request):
    now = datetime.now()
    if request.user.is_authenticated:
        slots = Slot.objects.filter(admin=request.user)
        slots = slots.order_by('date')
    else:
        slots = "Login to create a meeting slot."

    return render(request, "meetup/home.html", {
        "slots": slots,
        "now": now
    })


def setup(request):
    if request.method == "POST":
        admin_user = request.POST.get('setup-admin')
        admin_obj = User.objects.get(username=admin_user)
        slots = Slot.objects.filter(admin=admin_obj).all()
        has_slots = True
        if slots:
            is_booked = True
            for slot in slots:
                if not slot.booked:
                    is_booked = False
                    break
            return render(request, "meetup/setup2.html", {
                "slots": slots,
                "has_slots": has_slots,
                "is_booked":is_booked
            })
        else:
            has_slots = False
            return render(request, "meetup/setup2.html", {
                "has_slots": has_slots
            })

    else:
        return render(request, "meetup/setup.html")


def create_slot(request):
    if request.method == "POST":
        startTime = request.POST.get('start-time')
        endTime = request.POST.get('end-time')
        Date = request.POST.get('slot-date')
        slot = Slot.objects.create(
            admin=request.user, starttime=startTime, endtime=endTime, date=Date)
        slot.save()
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "meetup/create.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "meetup/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "meetup/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        name = request.POST["name"]
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "meetup/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.fullname = name
            user.save()
        except IntegrityError:
            return render(request, "meetup/register.html", {
                "message": "Username already taken."
            })

        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "meetup/register.html")
