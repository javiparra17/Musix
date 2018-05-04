from main.models import Musician
from django.shortcuts import render
from main.services import musician as service


def musicians(request):
    all_musicians = service.musicians()
    return render(request, 'musicians.html', {'musicians': all_musicians})
