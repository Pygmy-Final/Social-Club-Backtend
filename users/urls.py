from .views import  PeopleDetail , PeopleList , EventsDetail , EventsList
from django.urls import path

urlpatterns=[
    path('', PeopleList.as_view(),name='people_list'),
    path('events/', EventsList.as_view(),name='event_list')
]