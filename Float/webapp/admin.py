from django.contrib import admin
from webapp.models import Driver
from webapp.models import Trip

# Register your models here.

class DriverAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ['name',]

class TripAdmin(admin.ModelAdmin):
    list_display = ('id', 'driver_name')

    def driver_name(self, instance):
        return instance.driver.name

admin.site.register(Driver, DriverAdmin)
admin.site.register(Trip, TripAdmin)
