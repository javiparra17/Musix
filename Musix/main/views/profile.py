from main.models import Musician
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


def profile(request, musician_username):
    user = get_object_or_404(User, username=musician_username)
    musician = get_object_or_404(Musician, user=user)

    return render(request, 'profile.html', {'musician': musician})
