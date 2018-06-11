from main.models import Instrument
import main.functions as functions


def create_instrument(name, image):
    check_instrument = Instrument.objects.filter(name=name)
    if len(check_instrument) == 0:
        instrument = Instrument.objects.create(name=name, image=image)
    else:
        return "This instrument already exists"

    return instrument


def instruments():
    all_instruments = Instrument.objects.all()

    return all_instruments


def edit_instrument(instrument, name, image):
    path = "/static/media/" + str(instrument.image)
    functions.delete_file(path)

    instrument.name = name
    instrument.image = image

    instrument.save()


def delete_instrument(instrument):
    used_instruments = functions.get_all_used_instruments()

    if instrument not in used_instruments:
        image = instrument.image
        path = "/static/media/" + str(image)
        functions.delete_file(path)

        instrument.delete()

    else:
        return "You can not delete an used instrument"
