from django.contrib import admin
from base.models import Venue

class VenueAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'status']
    #prepopulated_fields = {"slug": ("name", )}

admin.site.register(Venue, VenueAdmin)