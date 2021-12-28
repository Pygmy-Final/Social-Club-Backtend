from django.shortcuts import render
from .models import People , Event
# from rest_framework.generics import (
#     ListCreateAPIView,
#     RetrieveUpdateDestroyAPIView,
# )
from django.views.generic import ListView , DetailView
# Create your views here.

class PeopleList(ListView):
    # queryset = User.objects.all()
    model=People
    fields = ['firstname', 'lastname', 'email','phonenumber','interests']

class PeopleDetail(DetailView):
    # queryset = User.objects.all()
    model=People
    fields = ['firstname', 'lastname', 'email','phonenumber','interests']

class EventsList(ListView):
    # queryset = User.objects.all()
    model=Event
    fields = ['EventName','EventCreator']

class EventsDetail(DetailView):
    # queryset = User.objects.all()
    model=Event
    fields = ['EventName','EventCategory','EventLocation','EventStartTime','EventDescription']