from django.test import TestCase
from main.tests import test_user as setup
from main.services import profile as service
from django.contrib.auth.models import User
from main.models import Musician


class ProfileTest(TestCase):
    def setUp(self):
        setup.set_up_musician_no_premium()

    def test_edit_profile(self):
        user = User.objects.get(username="musician1")
        musician = Musician.objects.get(user=user)

        name = "Edited"
        surname = "Edited"
        description = "Edited"
        photo = "Edited.jpg"
        phone = "123456789"
        gender = "M"
        country = "ES"
        city = "Edited"

        edited = service.edit_profile(musician, name, surname, description,
                                      photo, phone, gender, country, city)

        self.assertEquals(edited.description, description)
        self.assertEquals(edited.description, description)

    def test_change_password(self):
        user = User.objects.get(username="musician1")
        musician = Musician.objects.get(user=user)

        new_password = "newpassword"

        edited = service.change_password(musician, new_password)

        self.assertNotEquals(edited.user.password, user.password)
