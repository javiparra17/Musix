from main.models import Musician
from django.shortcuts import render

def musicians(request):
    musicians = Musician.objects.all()
    return render(request, 'musicians.html', {'musicians': musicians})