import os
from django.http import HttpResponse


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
