from django.db import models
from django.contrib.auth.models import AbstractUser
from shortuuid.django_fields import ShortUUIDField
from django.db.models.signals import post_save


GENDER = (
    ("Female", "Female"),
    ("Male", "Male"),
    ("Other", "Other"),
)

def user_directory_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (instance.user.id, filename)

class UserAccount(AbstractUser):
    email = models.EmailField(unique=True, max_length=500)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER, default='Other')
    otp = models.CharField(max_length=100, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    
    # def save(self, *args, **kwargs):
    #     email_username, _ = self.email.split('@')
    #     if self.username == '' or self.username == None:
    #         self.username = email_username
        
    #     super(UserAccount, self).save(*args, **kwargs)

class Profile(models.Model):
    p_id = ShortUUIDField(length=7, max_length=25, alphabet='abcdefghijklmnopqrstuvwxyz')
    image = models.FileField(upload_to=user_directory_path, default="default.jpg", null=True, blank=True)
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    country = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)

    wallet = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    is_verified = models.BooleanField(default=False)

    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        if self.user.user_name:
            return f'{self.user.username}'
        else:
            return f'{self.user.email}'

def create_user_profile(sender, instance, created, **kwargs):
    if not created:
        return
    Profile.objects.get_or_create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=UserAccount)
post_save.connect(save_user_profile, sender=UserAccount)