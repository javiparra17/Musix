from django.contrib.auth.models import User
from main import models
from django.utils.dateparse import parse_date
import django.core.management as djangocmd
from django.core.management.base import BaseCommand
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Command(BaseCommand):
    args = 'none'
    help = 'Populate the database'

    def _populate(self):

        # ADMINISTRATOR

        admin_user = User.objects.create_user(email='admin@musix.com',
                                              username='admin',
                                              password='admin')
        admin_user.save()
        admin = models.Administrator(user=admin_user)
        admin.save()

        # MUSICIAN

        userM1 = User.objects.create_user(first_name='musician1Name',
                                          last_name='musician1Surname',
                                          email='musician1@hotmail.com',
                                          username='musician1',
                                          password='musician1')
        userM1.save()
        musician1 = models.Musician(user=userM1,
                                    gender='M',
                                    description="Description1",
                                    country='ES',
                                    city='City1',
                                    registrationDate=parse_date('2017-07-15'),
                                    premium=False)
        musician1.save()

        userM2 = User.objects.create_user(first_name='musician2Name',
                                          last_name='musician2Surname',
                                          email='musician2@hotmail.com',
                                          username='musician2',
                                          password='musician2')
        userM2.save()
        musician2 = models.Musician(user=userM2,
                                    gender='M',
                                    description="Description2",
                                    country='ES',
                                    city='City2',
                                    registrationDate=parse_date('2018-01-04'),
                                    premium=True)
        musician2.save()

        # INSTRUMENT

        instrument1 = models.Instrument(name="Acoustic guitar", image="instruments/acousticGuitar.png")
        instrument1.save()

        instrument2 = models.Instrument(name="Bass", image="instruments/bass.png")
        instrument2.save()

        instrument3 = models.Instrument(name="Cello", image="instruments/cello.png")
        instrument3.save()

        instrument4 = models.Instrument(name="Clarinet", image="instruments/clarinet.png")
        instrument4.save()

        instrument5 = models.Instrument(name="Drums", image="instruments/drums.png")
        instrument5.save()

        instrument6 = models.Instrument(name="Electric guitar", image="instruments/electricGuitar.png")
        instrument6.save()

        instrument7 = models.Instrument(name="Piano", image="instruments/piano.png")
        instrument7.save()

        instrument8 = models.Instrument(name="Violin", image="instruments/violin.png")
        instrument8.save()

        # SONG

        song1 = models.Song(name="song1", author="author1", description="description1", additionalInstruments="N",
                            finished=False, creator=musician2)
        song1.save()
        song1.requiredInstruments.add(instrument1)
        song1.requiredInstruments.add(instrument2)
        song1.save()

    def handle(self, *args, **options):
        djangocmd.call_command('flush', interactive=False)
        djangocmd.call_command('migrate')
        print "Populating database..."
        self._populate()
        print "All is OK"
