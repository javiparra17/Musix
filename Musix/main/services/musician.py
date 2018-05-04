from main.models import Musician


def musicians():
    all_musicians = Musician.objects.all()
    return all_musicians