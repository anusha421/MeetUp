from django.db import models
from django.contrib.auth.models import AbstractUser

# user

# time slots
# 	owner
#   title
# 	starttime
#   endtime
# 	date
# 	booked bool
# 	booked with
#   meet link
	

class User(AbstractUser):
    fullname = models.TextField(blank=False)


class Slot(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    public = models.ForeignKey(User, on_delete=models.CASCADE, related_name="meeter", blank=True, null=True)
    title = models.TextField(blank=True)
    starttime = models.TimeField()
    endtime = models.TimeField()
    date = models.DateField()
    booked = models.BooleanField(default=False)

    def serialize(self):
        return {
            "id": self.id,
            "owner": self.user.username,
            "meeter": self.user.username,
            "title": self.title,
            "starttime": self.starttime.strftime("%I:%M %p"),
            "endtime": self.endtime.strftime("%I:%M %p"),
            "date": self.date.strftime("%b %d %Y"),
            "booked": self.booked,
        }