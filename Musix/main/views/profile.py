from main.models import Musician
from django.shortcuts import render


def profile(request, musician_id):
    musician = Musician.objects.get(id=musician_id)
    return render(request, 'profile.html', {'musician': musician})
