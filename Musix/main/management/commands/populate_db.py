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
                                    description="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu",
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

        user5 = User.objects.create_user(first_name='Mónica',
                                         last_name='Fernández Sanz',
                                         email='musician5@hotmail.com',
                                         username='musician5',
                                         password='musician5')
        user5.save()
        musician5 = models.Musician(user=user5,
                                    gender='F',
                                    description="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu",
                                    country='',
                                    city='',
                                    registrationDate=parse_date('2017-09-03'),
                                    premium=False)
        musician5.save()

        user6 = User.objects.create_user(first_name='Sancho',
                                         last_name='Molino Fernández',
                                         email='musician6@hotmail.com',
                                         username='musician6',
                                         password='musician6')
        user6.save()
        musician6 = models.Musician(user=user6,
                                    gender='M',
                                    description="",
                                    country='ES',
                                    city='Murcia',
                                    registrationDate=parse_date('2017-12-20'),
                                    premium=False)
        musician6.save()

        user7 = User.objects.create_user(first_name='Eva',
                                         last_name='Ramírez Morón',
                                         email='musician7@hotmail.com',
                                         username='musician7',
                                         password='musician7')
        user7.save()
        musician7 = models.Musician(user=user7,
                                    gender='F',
                                    description="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel.",
                                    country='ES',
                                    city='Navalmoral de la Mata',
                                    registrationDate=parse_date('2017-08-01'),
                                    premium=True)
        musician7.save()

        user8 = User.objects.create_user(first_name='Ramona',
                                         last_name='Domínguez Perogil',
                                         email='musician8@hotmail.com',
                                         username='musician8',
                                         password='musician8')

        user8.save()
        musician8 = models.Musician(user=user8,
                                    gender='F',
                                    description="",
                                    country='ES',
                                    city='Guadalajara',
                                    registrationDate=parse_date('2017-08-19'),
                                    premium=False)
        musician8.save()

        user9 = User.objects.create_user(first_name='Jacobo',
                                         last_name='Gustos Túnez',
                                         email='musician9@hotmail.com',
                                         username='musician9',
                                         password='musician9')
        user9.save()
        musician9 = models.Musician(user=user9,
                                    gender='M',
                                    description="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes.",
                                    country='ES',
                                    city='Valencia',
                                    registrationDate=parse_date('2017-05-03'),
                                    premium=False)
        musician9.save()

        user10 = User.objects.create_user(first_name='Raquel',
                                          last_name='Adame Martínez',
                                          email='musician10@hotmail.com',
                                          username='musician10',
                                          password='musician10')
        user10.save()
        musician10 = models.Musician(user=user10,
                                     photo="photos/Foto_Raquel.jpg",
                                     gender='F',
                                     description="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu",
                                     country='ES',
                                     city='Fregenal de la Sierra',
                                     registrationDate=parse_date('2017-11-22'),
                                     premium=True)
        musician10.save()

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

        instrument5 = models.Instrument(name="Contrabass",
                                        image="instruments/contrabass.png")
        instrument5.save()

        instrument6 = models.Instrument(name="Drums",
                                        image="instruments/drums.png")
        instrument6.save()

        instrument7 = models.Instrument(name="Electric guitar",
                                        image="instruments/electricGuitar.png")
        instrument7.save()

        instrument8 = models.Instrument(name="Flute",
                                        image="instruments/flute.png")
        instrument8.save()

        instrument9 = models.Instrument(name="Harp",
                                        image="instruments/harp.png")
        instrument9.save()

        instrument10 = models.Instrument(name="Oboe",
                                         image="instruments/oboe.png")
        instrument10.save()

        instrument11 = models.Instrument(name="Piano",
                                         image="instruments/piano.png")
        instrument11.save()

        instrument12 = models.Instrument(name="Saxophone",
                                         image="instruments/saxophone.png")
        instrument12.save()

        instrument13 = models.Instrument(name="Trombone",
                                         image="instruments/trombone.png")
        instrument13.save()

        instrument14 = models.Instrument(name="Trumpet",
                                         image="instruments/trumpet.png")
        instrument14.save()

        instrument15 = models.Instrument(name="Tube",
                                         image="instruments/tube.png")
        instrument15.save()

        instrument16 = models.Instrument(name="Violin",
                                         image="instruments/violin.png")
        instrument16.save()

        instrument17 = models.Instrument(name="Xylophone",
                                         image="instruments/xylophone.png")
        instrument17.save()

        # SONG

        song1 = models.Song(name="Bohemian rhapsody", author="Queen",
                            tune="B", accidental="b", tonality="M", bpm=78,
                            description="An amazing song of Queen",
                            additionalInstruments=False, finished=False,
                            creator=musician2)
        song1.save()
        song1.requiredInstruments.add(instrument2)
        song1.requiredInstruments.add(instrument6)
        song1.requiredInstruments.add(instrument7)
        song1.requiredInstruments.add(instrument11)
        song1.save()

        song2 = models.Song(name="I dreamed a dream", author="Les Miserables",
                            tune="E", accidental="b", tonality="M", bpm=80,
                            description="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes.",
                            additionalInstruments=True,
                            finished=False, creator=musician2)
        song2.save()

        song2.requiredInstruments.add(instrument3)
        song2.requiredInstruments.add(instrument4)
        song2.requiredInstruments.add(instrument5)
        song2.requiredInstruments.add(instrument8)
        song2.requiredInstruments.add(instrument11)
        song2.requiredInstruments.add(instrument16)
        song2.save()

        song3 = models.Song(name="Yellow submarine", author="The Beatles",
                            tune="D", tonality="M", bpm=100,
                            description="A song of The Beatles",
                            additionalInstruments=True,
                            finished=True, creator=musician2,
                            finishedSong="songs/Yellow submarine.mp3")
        song3.save()

        song3.requiredInstruments.add(instrument1)
        song3.requiredInstruments.add(instrument2)
        song3.requiredInstruments.add(instrument6)
        song3.requiredInstruments.add(instrument11)
        song3.save()

        song4 = models.Song(name="Waka waka", author="Shakira",
                            tune="D", tonality="M", bpm=125,
                            description="La canción del mundial de fútbol de "
                                        "Sudáfrica 2010",
                            additionalInstruments=True,
                            finished=False, creator=musician3)
        song4.save()

        song4.requiredInstruments.add(instrument2)
        song4.requiredInstruments.add(instrument11)
        song4.requiredInstruments.add(instrument17)
        song4.save()

        song5 = models.Song(name="Jueves", author="La Oreja de Van Gogh",
                            tune="F", tonality="M", bpm=100,
                            description="La canción que este grupo dedicó a las víctimas del atentado"
                                        " del 11M en 2004 en Madrid",
                            additionalInstruments=False,
                            finished=False, creator=musician7)
        song5.save()

        song5.requiredInstruments.add(instrument11)
        song5.save()

        song6 = models.Song(name="Thriller", author="Michael Jackson",
                            tune="C", accidental="#", tonality="m", bpm=120,
                            description="An amazing song of Michael Jackson. I love it",
                            additionalInstruments=True,
                            finished=False, creator=musician2)
        song6.save()

        song6.requiredInstruments.add(instrument2)
        song6.requiredInstruments.add(instrument6)
        song6.requiredInstruments.add(instrument11)
        song6.save()

        # TRACKS

        track1 = models.Track(sound="tracks/Bohemian Rhapsody piano.mp3",
                              status="P", instrument=instrument11,
                              musician=musician1, song=song1)
        track1.save()

        track2 = models.Track(sound="tracks/Bohemian Rhapsody bajo.mp3",
                              status="P", instrument=instrument2,
                              musician=musician3, song=song1)
        track2.save()

        track3 = models.Track(sound="tracks/Bohemian Rhapsody bateria.mp3",
                              status="P", instrument=instrument6,
                              musician=musician4, song=song1)
        track3.save()

        track4 = models.Track(sound="tracks/Jueves piano.mp3",
                              status="P", instrument=instrument11,
                              musician=musician2, song=song5)
        track4.save()


    def handle(self, *args, **options):
        djangocmd.call_command('flush', interactive=False)
        djangocmd.call_command('migrate')
        print "Populating database..."
        self._populate()
        print "All is OK"
