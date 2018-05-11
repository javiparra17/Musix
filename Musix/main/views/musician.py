from main.models import Musician
from django.shortcuts import render
from main.services import musician as service


def musicians(request):
    user = request.user
    musician = Musician.objects.get(user=user)

    all_musicians = service.musicians(musician)

    return render(request, 'musicians.html', {'musicians': all_musicians})
