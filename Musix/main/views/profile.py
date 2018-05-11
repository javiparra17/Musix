from main.models import Musician
from django.shortcuts import render
from django.contrib.auth.models import User

def profile(request, musician_username):
    user = User.objects.get(username=musician_username)
    musician = Musician.objects.get(user=user)
    return render(request, 'profile.html', {'musician': musician})
