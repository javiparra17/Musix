from django.test import TestCase
from main.tests import test_user as setup
from main.services import song as service
from django.contrib.auth.models import User
from main.models import Musician, Song, Track, Instrument


class SongTest(TestCase):
    def setUp(self):
        setup.set_up_musician_no_premium()
        setup.set_up_musician_premium()

    def test_create_song(self):
        user2 = User.objects.get(username="musician2")
        musician2 = Musician.objects.get(user=user2)

        name = "Name"
        author = "Author"
        tune = "F"
        accidental = "#"
        tonality = "M"
        bpm = 120
        description = "Description"
        score = "score.pdf"
        required_instruments = []
        additional_instruments = True

        song = service.create_song(name, author, tune, accidental, tonality,
                                   bpm, description, score,
                                   required_instruments, additional_instruments,
                                   musician2)

        song_saved = Song.objects.get(id=song.id)

        self.assertEquals(song_saved.name, name)
        self.assertEquals(song_saved.bpm, bpm)

        return song

    def test_finish_song(self):
        user2 = User.objects.get(username="musician2")
        musician2 = Musician.objects.get(user=user2)
        song = self.test_create_song()

        service.finish_song(musician2, song)

        self.assertEquals(song.finished, True)

    def test_negative_finish_song(self):
        user2 = User.objects.get(username="musician2")
        musician2 = Musician.objects.get(user=user2)
        song = self.test_create_song()

        song.finished = True
        song.save()

        result = service.finish_song(musician2, song)

        self.assertEquals(result, "This song is already finished")

    def test_reopen_song(self):
        user2 = User.objects.get(username="musician2")
        musician2 = Musician.objects.get(user=user2)
        song = self.test_create_song()

        song.finished = True
        song.save()

        service.reopen_song(musician2, song)

        self.assertEquals(song.finished, False)

    def test_negative_reopen_song(self):
        user2 = User.objects.get(username="musician2")
        musician2 = Musician.objects.get(user=user2)
        song = self.test_create_song()

        result = service.reopen_song(musician2, song)

        self.assertEquals(result, "This song is already opened")

    def test_publish_song(self):
        song = self.test_create_song()

        sound = "song.mp3"

        finished_song = service.publish_song(song, sound)

        self.assertEquals(finished_song.finishedSong, sound)

    def test_edit_song(self):
        song = self.test_create_song()

        name = "Edited"
        author = "Edited"
        tune = "F"
        accidental = "#"
        tonality = "M"
        bpm = 120
        description = "Edited"
        score = "score.pdf"
        required_instruments = []
        additional_instruments = True

        edited_song = service.edit_song(song, name, author, tune, accidental,
                                        tonality, bpm, description, score,
                                        required_instruments,
                                        additional_instruments)

        self.assertEquals(edited_song.name, name)
        self.assertEquals(edited_song.author, author)

    def test_negative_edit_song(self):
        song = self.test_create_song()
        song.finished = True
        song.save()

        name = "Edited"
        author = "Edited"
        tune = "F"
        accidental = "#"
        tonality = "M"
        bpm = 120
        description = "Edited"
        score = "score.pdf"
        required_instruments = []
        additional_instruments = True

        result = service.edit_song(song, name, author, tune, accidental,
                                   tonality, bpm, description, score,
                                   required_instruments,
                                   additional_instruments)

        self.assertEquals(result, "You can not edit a finished song")

    def test_negative_delete_song1(self):
        user1 = User.objects.get(username="musician1")
        musician1 = Musician.objects.get(user=user1)
        user2 = User.objects.get(username="musician2")
        musician2 = Musician.objects.get(user=user2)

        song = self.test_create_song()

        instrument1 = Instrument.objects.create(name="Prueba",
                                                image="instrument.jpg")
        Track.objects.create(sound="track.mp3", status="P",
                             instrument=instrument1, musician=musician1,
                             song=song)

        result = service.delete_song(musician2, song)

        self.assertEquals(result, "You can't delete an open song")

    def test_negative_delete_song2(self):
        user1 = User.objects.get(username="musician1")
        musician1 = Musician.objects.get(user=user1)
        user2 = User.objects.get(username="musician2")
        musician2 = Musician.objects.get(user=user2)

        song = self.test_create_song()

        instrument1 = Instrument.objects.create(name="Prueba",
                                                image="instrument.jpg")
        Track.objects.create(sound="track.mp3", status="P",
                             instrument=instrument1, musician=musician1,
                             song=song)
        song.finished = True
        song.save()

        result = service.delete_song(musician2, song)

        self.assertEquals(result, "This song has pending tracks")

    def test_delete_song(self):
        user2 = User.objects.get(username="musician2")
        musician2 = Musician.objects.get(user=user2)

        song = self.test_create_song()

        service.delete_song(musician2, song)

        songs = Song.objects.all()

        self.assertFalse(song in songs)
