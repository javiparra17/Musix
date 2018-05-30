from django.db import models
from django.contrib.auth.models import User
import main.choices as choices
from django.core.validators import MinValueValidator, MaxValueValidator

ACCIDENTALS = choices.ACCIDENTALS
COUNTRIES = choices.COUNTRIES
GENDERS = choices.GENDERS
STATUS = choices.STATUS
TONALITIES = choices.TONALITIES
TUNES = choices.TUNES


class Actor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Administrator(Actor):
    pass


class Instrument(models.Model):
    name = models.CharField(max_length=100, blank=False)
    image = models.ImageField(blank=False, upload_to='instruments')


class Musician(Actor):
    phone = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=7, blank=True, choices=GENDERS)
    description = models.TextField(max_length=500, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='photos')
    country = models.CharField(max_length=100, blank=True, choices=COUNTRIES)
    city = models.CharField(max_length=100, blank=True)
    registrationDate = models.DateField()
    premium = models.BooleanField(default=False, null=False)
    banned = models.BooleanField(default=False, null=False)


class Report(models.Model):
    description = models.TextField(max_length=500, blank=False)
    processed = models.BooleanField(default=False, null=False)
    affected = models.ForeignKey(Musician, on_delete=models.DO_NOTHING,
                                 null=False, related_name='affected')
    reported = models.ForeignKey(Musician, on_delete=models.DO_NOTHING,
                                 null=False, related_name='reported')


class Song(models.Model):
    name = models.CharField(max_length=20, blank=False)
    author = models.CharField(max_length=30, blank=False)
    tune = models.CharField(max_length=10, blank=False, choices=TUNES)
    accidental = models.CharField(max_length=10, blank=True,
                                  choices=ACCIDENTALS)
    tonality = models.CharField(max_length=10, blank=False, choices=TONALITIES)
    bpm = models.IntegerField(null=False, validators=[MinValueValidator(0),
                                                      MaxValueValidator(500)])
    description = models.TextField(max_length=500, blank=False)
    additionalInstruments = models.BooleanField(null=False)
    score = models.FileField(blank=True, upload_to='scores', null=True)
    finished = models.BooleanField(default=False, null=False)
    finishedSong = models.FileField(blank=True, upload_to='songs', null=True)

    creator = models.ForeignKey(Musician, on_delete=models.DO_NOTHING,
                                null=True)
    requiredInstruments = models.ManyToManyField(Instrument, blank=True)

    @property
    def song_tune(self):
        if self.accidental:
            if self.tonality == "m":
                res = str(self.tune) + str(self.accidental) + str(self.tonality)
            else:
                res = str(self.tune) + str(self.accidental)
        else:
            if self.tonality == "m":
                res = str(self.tune) + str(self.tonality)
            else:
                res = str(self.tune)
        return res


class Track(models.Model):
    sound = models.FileField(blank=False, upload_to='tracks', null=False)
    status = models.CharField(blank=False, max_length=20, choices=STATUS)

    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE,
                                   null=False)
    musician = models.ForeignKey(Musician, on_delete=models.DO_NOTHING,
                                 null=True)
    song = models.ForeignKey(Song, on_delete=models.DO_NOTHING, null=False)
