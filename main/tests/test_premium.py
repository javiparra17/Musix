from django.test import TestCase
from main.tests import test_user as setup
from main.services import premium as service
from django.contrib.auth.models import User
from main.models import Musician


class PremiumTest(TestCase):
    def setUp(self):
        setup.set_up_musician_no_premium()
        setup.set_up_musician_premium()

    def test_negative_become_premium(self):
        user = User.objects.get(username="musician2")
        musician = Musician.objects.get(user=user)
        result = service.become_premium(musician)

        self.assertEquals(result, "You are already premium")

    def test_become_premium(self):
        user = User.objects.get(username="musician1")
        musician = Musician.objects.get(user=user)
        result = service.become_premium(musician)

        self.assertEquals(result.premium, True)
