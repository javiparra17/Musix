import os

def upload_file(file):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)


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
