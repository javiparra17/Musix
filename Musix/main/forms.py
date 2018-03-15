# -*- encoding: utf-8 -*-
from django import forms
from models import *
import functions
import views
import choices
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

COUNTRIES = choices.COUNTRIES
GENDERS = choices.GENDERS
INSTRUMENTS = choices.INSTRUMENTS
YESORNOT = choices.YESORNOT

class MusicianForm(forms.ModelForm):
    name = forms.CharField(label="Name", widget=forms.TextInput, required=True)
    surname = forms.CharField(label="Surname", widget=forms.TextInput, required=True)
    username = forms.CharField(label="Username", widget=forms.TextInput, required=True)
    email = forms.EmailField(label="Email", widget=forms.TextInput, required=True)
    password = forms.CharField(label="Password", widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput, required=True)

    gender = forms.CharField(required=True, widget=forms.RadioSelect(choices=GENDERS))
    #birthdate = forms.DateField(widget=forms.SelectDateWidget)
    country = forms.CharField(required=True, widget=forms.Select(choices=COUNTRIES), initial="ES")

    class Meta:
        model = Musician
        fields = ('name', 'surname', 'username', 'email', 'gender', 'description', 'country', 'photo', 'city', 'password', 'password2')

    def save(self, commit=True):
        user = super(MusicianForm, self).save(commit=False)
        user.name = self.cleaned_data["name"]
        user.surname = self.cleaned_data["surname"]
        user.gender = self.cleaned_data["gender"]
        user.description = self.cleaned_data["description"]
        user.country = self.cleaned_data["country"]
        user.city = self.cleaned_data["city"]
        user.photo = self.cleaned_data["photo"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class CreateSongForm(forms.ModelForm):
    requiredInstruments = forms.CharField(required=True, widget=forms.CheckboxSelectMultiple(choices=INSTRUMENTS), label="Required instruments")
    additionalInstruments = forms.CharField(required=True, widget=forms.RadioSelect(choices=YESORNOT), label="Additional instruments?")

    class Meta:
        model = Song
        fields = ('name', 'author', 'description', 'requiredInstruments', 'additionalInstruments')

class TrackForm(forms.ModelForm):

    class Meta:
        model = Track
        fields = {'instrument', 'sound'}

class LoginForm(forms.ModelForm):
    email = forms.EmailField(required=True, max_length=40)
    password = forms.CharField(required=True, max_length=30, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')