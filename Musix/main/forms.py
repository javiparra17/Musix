# -*- encoding: utf-8 -*-
from django import forms
from main.models import *
import main.choices as choices

COUNTRIES = choices.COUNTRIES
GENDERS = choices.GENDERS
YESORNOT = choices.YESORNOT


class InstrumentForm(forms.ModelForm):
    class Meta:
        model = Instrument
        fields = ('name', 'image')


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", widget=forms.TextInput,
                               required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput,
                               required=True)


class MusicianForm(forms.ModelForm):
    name = forms.CharField(label="Name", widget=forms.TextInput, required=True)
    surname = forms.CharField(label="Surname", widget=forms.TextInput,
                              required=True)
    username = forms.CharField(label="Username", widget=forms.TextInput,
                               required=True)
    email = forms.EmailField(label="Email", widget=forms.TextInput,
                             required=True)
    password = forms.CharField(label="Password", widget=forms.PasswordInput,
                               required=True)
    password2 = forms.CharField(label="Confirm password",
                                widget=forms.PasswordInput, required=True)

    class Meta:
        model = Musician
        fields = ('name', 'surname', 'username', 'email', 'phone', 'photo',
                  'password', 'password2')


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('name', 'author', 'description', 'requiredInstruments',
                  'additionalInstruments')


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = {'instrument', 'sound'}
