from main.models import Musician
from django.shortcuts import render

def profile(request, musicianId):
    musician = Musician.objects.get(id=musicianId)
    return render(request, 'profile.html', {'musician': musician,})