from django.contrib import admin
from .models import flight_details
# Register your models here.
class FlightDetailsAdmin(admin.ModelAdmin):
    list_display = ['fname','fdate','ffare','fstart','fend']

admin.site.register(flight_details,FlightDetailsAdmin)
