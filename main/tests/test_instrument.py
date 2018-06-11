from django.test import TestCase
from main.tests import test_user as setup
from main.services import instrument as service
from main.models import Instrument


class InstrumentTest(TestCase):
    def setUp(self):
        setup.set_up_admin()

    def test_create_instrument(self):
        name = "Prueba"
        image = "prueba.jpg"

        instrument = service.create_instrument(name, image)

        instrument_saved = Instrument.objects.get(id=instrument.id)

        self.assertEquals(instrument_saved.name, name)
        self.assertEquals(instrument_saved.image, image)

    def test_negative_create_instrument(self):
        name = "Piano"
        image = "piano.jpg"

        service.create_instrument(name, image)

        result = service.create_instrument(name, image)

        self.assertEquals(result, "This instrument already exists")

    def test_edit_instrument(self):
        name = "Piano"
        image = "piano.jpg"

        instrument = service.create_instrument(name, image)

        new_name = "Edited"

        instrument.name = new_name
        instrument.save()

        edited = Instrument.objects.get(id=instrument.id)

        self.assertEquals(edited.name, new_name)

    def test_delete_instrument(self):
        name = "Piano"
        image = "piano.jpg"

        instrument = service.create_instrument(name, image)

        instrument.delete()

        instruments = Instrument.objects.all()

        self.assertFalse(instrument in instruments)
