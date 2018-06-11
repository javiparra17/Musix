import os
from django.http import HttpResponse
from main.models import Song, Track


def get_all_used_instruments():
    all_songs = Song.objects.all()
    all_tracks = Track.objects.all()

    used_instruments = []

    for s in all_songs:
        for i in s.requiredInstruments.all():
            if i not in used_instruments:
                used_instruments.append(i)
    for t in all_tracks:
        if t.instrument not in used_instruments:
            used_instruments.append(t.instrument)

    return used_instruments


def create_tuple_instruments(instruments):
    res = []
    for i in instruments:
        aux = (i.name, i.name)
        res.append(aux)
    return tuple(res)


def delete_file(path):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    root = BASE_DIR + path
    os.remove(root)


def download_track(path):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    root = BASE_DIR + "/static/media/" + path

    myfile = open(root).read()
    response = HttpResponse(myfile, content_type="audio/mpeg")
    response['Content-Disposition'] = 'attachment; filename=hola.mp3'

    return response
