from django.db import models
from django.contrib.auth.models import User
from django import forms
import main.choices as choices

COUNTRIES = choices.COUNTRIES
GENDERS = choices.GENDERS
INSTRUMENTS = choices.INSTRUMENTS
STATUS = choices.STATUS
YESORNOT = choices.YESORNOT

# Create your models here.

class Actor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Administrator(Actor):
    pass

class Musician(Actor):
    gender = models.CharField(max_length=7, blank=False, choices=GENDERS)
    description = models.TextField(max_length=500, blank=True)
    country = models.CharField(max_length=100, blank=False, choices=COUNTRIES, default='ES')
    photo = models.ImageField(null=True)
    city = models.CharField(max_length=50, blank=True)
    registrationDate = models.DateField(auto_now_add=True)
    premium = models.BooleanField(default=False, null=False)

class Song(models.Model):
    name = models.CharField(max_length=20, blank=False)
    author = models.CharField(max_length=30, blank=False)
    description = models.TextField(max_length=500, blank=False)
    requiredInstruments = models.TextField(max_length=10000, blank=True)
    additionalInstruments = models.CharField(blank=False, max_length=5, choices=YESORNOT)
    finished = models.BooleanField(default=False, null=False)

    creator = models.ForeignKey(Musician, on_delete=models.DO_NOTHING, null=True)

class Track(models.Model):
    instrument = models.CharField(blank=False, max_length=100, choices=INSTRUMENTS)
    sound = models.FileField(blank=False, upload_to='1', null=False)
    status = models.CharField(blank=False, max_length=20, choices=STATUS)

    musician = models.ForeignKey(Musician, on_delete=models.DO_NOTHING, null=True)
    song = models.ForeignKey(Song, on_delete=models.DO_NOTHING, null=False)