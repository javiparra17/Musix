from main.models import Musician


def musicians(musician):
    if musician:
        all_musicians = Musician.objects.exclude(id=musician.id)
    else:
        all_musicians = Musician.objects.all()

    return all_musicians
