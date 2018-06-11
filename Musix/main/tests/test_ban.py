from django.test import TestCase
from main.tests import test_user as setup
from main.services import ban as service
from django.contrib.auth.models import User
from main.models import Musician


class BanTest(TestCase):
    def setUp(self):
        setup.set_up_musician_no_premium()
        setup.set_up_musician_banned()

    def test_negative_unban_musician(self):
        user = User.objects.get(username="musician1")
        musician = Musician.objects.get(user=user)
        result = service.unban(musician)

        self.assertEquals(result, "This musician is not banned")

    def test_ban_musician(self):
        user = User.objects.get(username="musician1")
        musician = Musician.objects.get(user=user)
        service.ban(musician)

        self.assertEquals(musician.banned, True)

    def test_negative_ban_musician(self):
        user = User.objects.get(username="musician3")
        musician = Musician.objects.get(user=user)
        result = service.ban(musician)

        self.assertEquals(result, "This musician is already banned")

    def test_unban_musician(self):
        user = User.objects.get(username="musician3")
        musician = Musician.objects.get(user=user)
        service.unban(musician)

        self.assertEquals(musician.banned, False)
