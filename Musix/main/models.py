from django.db import models
from django.contrib.auth.models import User
from django import forms
import choices

COUNTRIES = choices.COUNTRIES
GENDERS = choices.GENDERS
INSTRUMENTS = choices.INSTRUMENTS
YESORNOT = choices.YESORNOT

# Create your models here.

class Actor(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)

class Person(Actor):
    registrationDate = models.DateField(auto_now_add=True)
    gender = models.CharField(max_length=7, blank=False, choices=GENDERS)
    description = models.TextField(max_length=500, blank=True)
    country = models.CharField(max_length=100, blank=False, choices=COUNTRIES, default='ES')
    photo = models.ImageField(null=True)
    #birthdate = models.DateField(null=True)
    city = models.CharField(max_length=50, blank=True)
    premium = models.BooleanField(default=False, null=False)

class Song(models.Model):
    name = models.CharField(max_length=20, blank=False)
    author = models.CharField(max_length=30, blank=False)
    description = models.TextField(max_length=500, blank=False)
    requiredInstruments = models.TextField(max_length=10000, blank=True)
    additionalInstruments = models.CharField(blank=False, max_length=5, choices=YESORNOT)
    finished = models.BooleanField(default=False, null=False)

    creator = models.ForeignKey(Person, on_delete=models.DO_NOTHING, null=True)

class Track(models.Model):
    instrument = models.CharField(blank=False, max_length=100, choices=INSTRUMENTS)
    sound = models.FileField(blank=False, upload_to='1', null=False)

    #user = models.ForeignKey(Person, on_delete=models.DO_NOTHING, null=True)
    #song = models.ForeignKey(Song, on_delete=models.DO_NOTHING, null=False)