from django.contrib import admin
from .models import People , Event

# Register your models here.
@admin.register(People)
class AdminPeople(admin.ModelAdmin):
    list_display=['firstname','lastname','email','id']

@admin.register(Event)
class AdminEvents(admin.ModelAdmin):
    list_display=['EventName','EventCreator','EventParticipants']
