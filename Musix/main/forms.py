# -*- encoding: utf-8 -*-
from django import forms
from main.models import *
import main.choices as choices

COUNTRIES = choices.COUNTRIES
GENDERS = choices.GENDERS
YESORNOT = choices.YESORNOT


class FinishedSongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('finishedSong',)


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


class PasswordEditForm(forms.Form):
    newPassword = forms.CharField(label="New password",
                                  widget=forms.PasswordInput, required=True)
    checkPassword = forms.CharField(label="Confirm new password",
                                    widget=forms.PasswordInput, required=True)


class ProfileEditForm(forms.ModelForm):
    name = forms.CharField(label="Name", widget=forms.TextInput, required=True)
    surname = forms.CharField(label="Surname", widget=forms.TextInput,
                              required=True)
    username = forms.CharField(label="Username", widget=forms.TextInput,
                               required=True)
    description = forms.CharField(label="Description", widget=forms.Textarea,
                                  required=False)
    gender = forms.CharField(label="Gender",
                             widget=forms.RadioSelect(choices=GENDERS),
                             required=False)
    country = forms.CharField(label="Country",
                              widget=forms.Select(choices=COUNTRIES),
                              required=False)
    city = forms.CharField(label="City", widget=forms.TextInput, required=False)

    class Meta:
        model = Musician
        fields = ('name', 'surname', 'username', 'phone', 'photo',
                  'description', 'gender', 'country', 'city')


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('name', 'author', 'tune', 'accidental', 'tonality', 'bpm',
                  'description', 'score', 'additionalInstruments',
                  'requiredInstruments')


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = {'instrument', 'sound'}
