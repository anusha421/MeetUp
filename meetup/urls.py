from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("home", views.home, name='home'),
    path("register", views.register, name='register'),
    path("setup", views.setup, name='setup'),
    path("createSlot", views.create_slot, name='create_slot'),
    path("login", views.login_view, name="login_view"),
    path("logout", views.logout_view, name="logout_view"),
]