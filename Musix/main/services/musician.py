from main.models import Musician


def musicians(musician):
    all_musicians = Musician.objects.exclude(id=musician.id)
    return all_musicians