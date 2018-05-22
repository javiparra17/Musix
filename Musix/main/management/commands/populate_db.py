# -*- encoding: utf-8 -*-

from django.contrib.auth.models import User
from main import models
from django.utils.dateparse import parse_date
import django.core.management as djangocmd
from django.core.management.base import BaseCommand
import os

BASE_DIR = \
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


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

        user1 = User.objects.create_user(first_name='Víctor',
                                         last_name=' Moya',
                                         email='musician1@hotmail.com',
                                         username='musician1',
                                         password='musician1')
        user1.save()
        musician1 = models.Musician(user=user1,
                                    gender='M',
                                    description="Description1",
                                    country='ES',
                                    city='Madrid',
                                    registrationDate=parse_date('2017-07-15'),
                                    premium=False)
        musician1.save()

        user2 = User.objects.create_user(first_name='Javier',
                                         last_name='Parra',
                                         email='musician2@hotmail.com',
                                         username='musician2',
                                         password='musician2')
        user2.save()
        musician2 = models.Musician(user=user2,
                                    gender='M',
                                    description="Description2",
                                    country='ES',
                                    city='Fregenal de la Sierra',
                                    registrationDate=parse_date('2018-01-04'),
                                    premium=True)
        musician2.save()

        user3 = User.objects.create_user(first_name='Alicia',
                                         last_name='Vázquez',
                                         email='musician3@hotmail.com',
                                         username='musician3',
                                         password='musician3')
        user3.save()
        musician3 = models.Musician(user=user3,
                                    gender='F',
                                    description="Description3",
                                    country='ES',
                                    city='Valencia',
                                    registrationDate=parse_date('2018-01-28'),
                                    premium=True)
        musician3.save()

        user4 = User.objects.create_user(first_name='Miguel',
                                         last_name='Montes',
                                         email='musician4@hotmail.com',
                                         username='musician4',
                                         password='musician4')
        user4.save()
        musician4 = models.Musician(user=user4,
                                    gender='M',
                                    description="Description4",
                                    country='ES',
                                    city='Badajoz',
                                    registrationDate=parse_date('2017-02-15'),
                                    premium=False)
        musician4.save()

        # INSTRUMENT

        instrument1 = models.Instrument(name="Acoustic guitar",
                                        image="instruments/acousticGuitar.png")
        instrument1.save()

        instrument2 = models.Instrument(name="Bass",
                                        image="instruments/bass.png")
        instrument2.save()

        instrument3 = models.Instrument(name="Cello",
                                        image="instruments/cello.png")
        instrument3.save()

        instrument4 = models.Instrument(name="Clarinet",
                                        image="instruments/clarinet.png")
        instrument4.save()

        instrument5 = models.Instrument(name="Drums",
                                        image="instruments/drums.png")
        instrument5.save()

        instrument6 = models.Instrument(name="Electric guitar",
                                        image="instruments/electricGuitar.png")
        instrument6.save()

        instrument7 = models.Instrument(name="Piano",
                                        image="instruments/piano.png")
        instrument7.save()

        instrument8 = models.Instrument(name="Violin",
                                        image="instruments/violin.png")
        instrument8.save()

        # SONG

        song1 = models.Song(name="Bohemian rhapsody", author="Queen",
                            description="An amazing song of Queen",
                            additionalInstruments=False, finished=False,
                            creator=musician2)
        song1.save()
        song1.requiredInstruments.add(instrument2)
        song1.requiredInstruments.add(instrument5)
        song1.requiredInstruments.add(instrument6)
        song1.requiredInstruments.add(instrument7)
        song1.save()

        song2 = models.Song(name="I dreamed a dream", author="Les Miserables",
                            description="A song of the film Les Miserables",
                            additionalInstruments=True,
                            finished=False, creator=musician2)
        song2.save()

        song2.requiredInstruments.add(instrument3)
        song2.requiredInstruments.add(instrument4)
        song2.requiredInstruments.add(instrument7)
        song2.requiredInstruments.add(instrument8)
        song2.save()

        song3 = models.Song(name="Yellow submarine", author="The Beatles",
                            description="A song of The Beatles",
                            additionalInstruments=False,
                            finished=True, creator=musician2,
                            finishedSong="songs/Yellow submarine.mp3")
        song3.save()

        song3.requiredInstruments.add(instrument1)
        song3.requiredInstruments.add(instrument2)
        song3.requiredInstruments.add(instrument5)
        song3.requiredInstruments.add(instrument7)
        song3.save()

        song4 = models.Song(name="Tu canción", author="Alfred y Amaia",
                            description="La canción que representará a España "
                                        "en Eurovisión 2018",
                            additionalInstruments=True,
                            finished=False, creator=musician3)
        song4.save()

        song4.requiredInstruments.add(instrument1)
        song4.requiredInstruments.add(instrument2)
        song4.requiredInstruments.add(instrument5)
        song4.requiredInstruments.add(instrument7)
        song4.save()

        # TRACKS

        track1 = models.Track(sound="tracks/Bohemian Rhapsody piano.mp3",
                              status="P", instrument=instrument7,
                              musician=musician1, song=song1)
        track1.save()

        track2 = models.Track(sound="tracks/Bohemian Rhapsody bajo.mp3",
                              status="P", instrument=instrument2,
                              musician=musician3, song=song1)
        track2.save()

        track3 = models.Track(sound="tracks/Bohemian Rhapsody batería.mp3",
                              status="P", instrument=instrument5,
                              musician=musician4, song=song1)
        track3.save()

    def handle(self, *args, **options):
        djangocmd.call_command('flush', interactive=False)
        djangocmd.call_command('migrate')
        print "Populating database..."
        self._populate()
        print "All is OK"
