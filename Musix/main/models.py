from django.db import models
from django.contrib.auth.models import User
import main.choices as choices

COUNTRIES = choices.COUNTRIES
GENDERS = choices.GENDERS
STATUS = choices.STATUS
YESORNOT = choices.YESORNOT

# Create your models here.

class Actor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Administrator(Actor):
    pass

class Instrument(models.Model):
    name = models.CharField(max_length=100, blank=False)
    image = models.ImageField(blank=False, upload_to='instruments')

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
    additionalInstruments = models.CharField(blank=False, max_length=5, choices=YESORNOT)
    finished = models.BooleanField(default=False, null=False)

    creator = models.ForeignKey(Musician, on_delete=models.DO_NOTHING, null=True)
    requiredInstruments = models.ManyToManyField(Instrument)

class Status(models.Model):
    status = models.CharField(blank=False, max_length=20, choices=STATUS)

class Track(models.Model):
    instrument = models.CharField(blank=False, max_length=100)
    sound = models.FileField(blank=False, upload_to='tracks', null=False)

    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, null=False)
    musician = models.ForeignKey(Musician, on_delete=models.DO_NOTHING, null=True)
    song = models.ForeignKey(Song, on_delete=models.DO_NOTHING, null=False)