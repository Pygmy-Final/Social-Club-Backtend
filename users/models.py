from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import IntegerField
from multiselectfield import MultiSelectField
# from django.db.models import IntegerField, Model
from django_mysql.models import ListTextField

class People(models.Model):
    firstname     = models.CharField(max_length=26)
    lastname      = models.CharField(max_length=26)
    email         = models.EmailField(max_length=256, unique=True)
    password      = models.CharField(max_length=26,null=True)
    #Email and Password should be used to create a profile 
    gender        = models.CharField(max_length=26,choices=[('Male', 'Male'), ('Female', 'Female')],default='Male')
    phonenumber   = IntegerField()
    profilePicture= models.ImageField(upload_to ='ProfilePictures/', default='ProfilePictures/default.jpg')
    interests     = MultiSelectField(max_length=26, choices=[  ('Reading', 'Reading'), ('Cycling', 'Cycling'),
                                                               ('Hiking','Hiking'), ('Drawing', 'Drawing'),('Photography', 'Photography'),
                                                               ('Swimming','Swimming'),('Sleeping','Sleeping'),('Sports','Sports'),('Gaming','Gaming')])
    def __str__(self):
        return str(self.id)
# return id so i can use it in the front end to render the name

class Event(models.Model):
    EventName        = models.CharField(max_length=256)
    EventDescription = models.CharField(max_length=256)
    EventLocation    = models.CharField(max_length=256)
    EventCategory    = MultiSelectField(max_length=26, choices=[  ('Reading', 'Reading'), ('Cycling', 'Cycling'),
                                                                  ('Hiking','Hiking'), ('Drawing', 'Drawing'),('Photography', 'Photography'),
                                                                  ('Swimming','Swimming'),('Sleeping','Sleeping'),('Sports','Sports'),('Gaming','Gaming')])
    EventStartTime  = models.DateTimeField()
    EventCreator    = models.ForeignKey(People,on_delete=models.CASCADE, null=True)
    EventParticipants = ListTextField(  base_field=IntegerField(),
                                        size=50,  null=True) 

                                        
    # EventParticipants = models.ForeignKey(People,on_delete=models.CASCADE, null=True) 
    # Update when typing and add the user into the participants
    # send array from the front to update the ids for the users who want to join the event
    # check https://django-mysql.readthedocs.io/en/latest/model_fields/list_fields.html 



