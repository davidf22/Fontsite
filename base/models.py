from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator

User = get_user_model()

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_booking')
    checkin_date = models.DateTimeField(auto_now_add=True, blank=True)
    checkout_date = models.DateTimeField(auto_now_add=True, blank=True)
    number_of_adults = models.IntegerField(null=True, blank=True, validators=[MaxValueValidator(20)])
    number_of_children = models.CharField(max_length=20, null=True, blank=True)


class Room(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='booking')


class BookingRoom(models.Model):
    room = models.ForeignKey(Booking, on_delete=models.CASCADE)