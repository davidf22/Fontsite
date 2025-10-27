from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.utils.html import mark_safe
from django.core.validators import MaxValueValidator
from shortuuid.django_fields import ShortUUIDField
import shortuuid

User = get_user_model()

HOTEL_STATUS = (
    ("Draft", "Draft"),
    ("Disabled", "Disabled"),
    ("Rejected", "Rejected"),
    ("In Review", "Draft"),
    ("Live", "Live"),
)

class Venue(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to="hotel_glallery")
    address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    email = models.EmailField(max_length=36)
    status = models.CharField(max_length=20, choices=HOTEL_STATUS)

    tags = models.CharField(max_length=200, help_text="Seperate tags with comma")
    views = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)
    hid = ShortUUIDField(unique=True, length=10, max_length=20, alphabet="abcdefghijklmnopqrstuvwxyz")
    slug = models.SlugField(unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug == None:
            uuid_key = shortuuid.uuid()
            uniqueid = uuid_key[:4]
            self.slug = slugify(self.name) + '-' + str(uniqueid.lower())

        super(Venue, self).save(*args, **kwargs)
    
    def thumbnail(self):
        return mark_safe("<img_src='%s' width='50' height='50' style='object-fit: cover; border-radius: 6px;' />" % (self.image.url))

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