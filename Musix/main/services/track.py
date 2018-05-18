from main.models import Track


def upload_track(instrument, sound, musician, song):
    track = Track.objects.create(instrument=instrument, sound=sound,
                                 musician=musician, song=song, status="P")

    return track


def my_tracks(musician):
    mytracks = Track.objects.filter(musician=musician)

    return mytracks


def tracks(song):
    tracks_song = Track.objects.filter(song=song)

    return tracks_song


def accept_track(track):
    if track.status == 'P':
        track.status = 'A'
        track.save()


def deny_track(track):
    if track.status == 'P':
        track.status = 'D'
        track.save()
