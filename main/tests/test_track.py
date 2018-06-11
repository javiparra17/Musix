from django.test import TestCase
from main.tests import test_user as setup
from main.services import song as service_song
from main.services import track as service
from django.contrib.auth.models import User
from main.models import Musician, Track, Instrument


class TrackTest(TestCase):
    def setUp(self):
        setup.set_up_musician_no_premium()
        setup.set_up_musician_premium()

    def test_upload_track(self):
        user1 = User.objects.get(username="musician1")
        musician1 = Musician.objects.get(user=user1)
        user2 = User.objects.get(username="musician2")
        musician2 = Musician.objects.get(user=user2)

        instrument1 = Instrument.objects.create(name="Instrument",
                                                image="instrument.jpg")

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

        song = service_song.create_song(name, author, tune, accidental,
                                        tonality, bpm, description, score,
                                        required_instruments,
                                        additional_instruments, musician2)

        sound = "sound.mp3"

        track = service.upload_track(instrument1, sound, musician1, song)

        track_saved = Track.objects.get(id=track.id)

        self.assertEquals(track_saved.sound, sound)

        return track

    def test_accept_track(self):
        track = self.test_upload_track()
        service.accept_track(track)

        self.assertEquals(track.status, "A")

    def test_deny_track(self):
        track = self.test_upload_track()
        service.deny_track(track)

        self.assertEquals(track.status, "D")

    def test_negative_delete_track(self):
        user1 = User.objects.get(username="musician1")
        musician1 = Musician.objects.get(user=user1)

        track = self.test_upload_track()
        track.status = "A"
        track.save()

        result = service.delete_track(musician1, track)

        self.assertEquals(result, "You can't delete an accepted track")

    def test_delete_track(self):
        track = self.test_upload_track()

        track.delete()

        tracks = Track.objects.all()

        self.assertFalse(track in tracks)
