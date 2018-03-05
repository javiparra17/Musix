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

class UserForm(UserCreationForm):
    name = forms.CharField(required=True, max_length=30)
    surname = forms.CharField(required=True, max_length=150)
    gender = forms.CharField(required=True, widget=forms.RadioSelect(choices=GENDERS))
    #birthdate = forms.DateField(widget=forms.SelectDateWidget)
    description = forms.CharField(required=False, widget=forms.Textarea, max_length=500)
    country = forms.CharField(required=True, widget=forms.Select(choices=COUNTRIES), initial="ES")
    city = forms.CharField(required=False)
    photo = forms.ImageField(required=False)
    email = forms.EmailField(required=True, max_length=40)

    class Meta:
        model = User
        fields = ('name', 'surname', 'gender', 'description', 'country', 'city', 'photo', 'email', 'username', 'password1', 'password2')

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
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
    name = forms.CharField(required=True, max_length=20)
    author = forms.CharField(required=True, max_length=30)
    description = forms.CharField(required=True, max_length=500, widget=forms.Textarea)
    requiredInstruments = forms.CharField(required=True, widget=forms.CheckboxSelectMultiple(choices=INSTRUMENTS), label="Required instruments")
    additionalInstruments = forms.BooleanField(required=True, widget=forms.RadioSelect(choices=YESORNOT), label="Additional instruments?")

    class Meta:
        model = Song
        fields = ('name', 'author', 'description', 'requiredInstruments', 'additionalInstruments')

class TrackForm(forms.ModelForm):
    instrument = forms.CharField(widget=forms.Select(choices=INSTRUMENTS))
    sound = forms.FileField(required=True)

    class Meta:
        model = Track
        fields = {'instrument'}

class LoginForm(forms.ModelForm):
    email = forms.EmailField(required=True, max_length=40)
    password = forms.CharField(required=True, max_length=30, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')