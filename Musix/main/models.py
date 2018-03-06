from django.db import models
from django.contrib.auth.models import User
from django import forms
import choices

COUNTRIES = choices.COUNTRIES
GENDERS = choices.GENDERS
INSTRUMENTS = choices.INSTRUMENTS

# Create your models here.

class InfoActor(models.Model):
    registrationDate = models.DateField(auto_now_add=True)
    gender = models.CharField(max_length=7, blank=False, choices=GENDERS)
    description = models.TextField(max_length=500, blank=True)
    country = models.CharField(max_length=100, blank=False, choices=COUNTRIES)
    photo = models.ImageField(blank=True)

class InfoUser(InfoActor):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #birthdate = models.DateField(blank=False)
    city = models.CharField(max_length=50, blank=True)
    premium = models.BooleanField(default=False)

class Song(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=20, blank=False)
    author = models.CharField(max_length=30, blank=False)
    description = models.TextField(max_length=500, blank=False)
    requiredInstruments = models.TextField(max_length=10000, blank=True)
    additionalInstruments = models.BooleanField()
    finished = models.BooleanField(default=False)

    #creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, unique=False)

class Track(models.Model):
    #id = models.IntegerField(primary_key=True, unique=True)
    instrument = models.CharField(blank=False, max_length=100)
    sound = models.FileField(blank=False, upload_to='1')

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # song = models.ForeignKey(Song, on_delete=models.CASCADE, null=False)