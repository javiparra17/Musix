from main.models import Musician
from django.shortcuts import render
from main.services import musician as service


def musicians(request):
    try:
        user = request.user
        musician = Musician.objects.get(user=user)

        all_musicians = service.musicians(musician)
    except:
        all_musicians = service.musicians(None)

    return render(request, 'musicians.html', {'musicians': all_musicians})
