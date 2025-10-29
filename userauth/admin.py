from django.contrib import admin
from userauth.models import UserAccount, Profile


# class UserAdmin(admin.ModelAdmin):
#     search_fields = ['username', 'email']
#     list_display = ['username', 'email', 'phone_number', 'gender']


class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'user__email']
    list_display = ['p_id', 'user', 'is_verified']

admin.site.register(UserAccount)
admin.site.register(Profile)