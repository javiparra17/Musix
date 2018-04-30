# -*- encoding: utf-8 -*-
from django import forms
from main.models import *
import main.choices as choices
import main.functions as functions

COUNTRIES = choices.COUNTRIES
GENDERS = choices.GENDERS
INSTRUMENTS = functions.createTupleInstruments(Instrument.objects.all())
YESORNOT = choices.YESORNOT

class InstrumentForm(forms.ModelForm):
    class Meta:
        model = Instrument
        fields = ('name', 'image')

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", widget=forms.TextInput, required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)

class MusicianForm(forms.ModelForm):
    name = forms.CharField(label="Name", widget=forms.TextInput, required=True)
    surname = forms.CharField(label="Surname", widget=forms.TextInput, required=True)
    username = forms.CharField(label="Username", widget=forms.TextInput, required=True)
    email = forms.EmailField(label="Email", widget=forms.TextInput, required=True)
    password = forms.CharField(label="Password", widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput, required=True)

    class Meta:
        model = Musician
        fields = ('name', 'surname', 'username', 'email', 'phone', 'photo', 'password', 'password2')

class SongForm(forms.ModelForm):
    requiredInstruments = forms.CharField(required=True, widget=forms.CheckboxSelectMultiple(choices=INSTRUMENTS), label="Required instruments")
    additionalInstruments = forms.CharField(required=True, widget=forms.RadioSelect(choices=YESORNOT), label="Additional instruments?")

    class Meta:
        model = Song
        fields = ('name', 'author', 'description', 'requiredInstruments', 'additionalInstruments')

class TrackForm(forms.ModelForm):
    instrument = forms.CharField(required=True, widget=forms.Select(choices=INSTRUMENTS), label="Required instruments")

    class Meta:
        model = Track
        fields = {'instrument', 'sound'}