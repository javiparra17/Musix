from main.models import Track
import main.functions as functions


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

def delete_track(musician, track):
    if track.musician == musician:
        if track.status == "P" or track.status == "D":
            sound = track.sound
            path = "/static/media/" + str(sound)
            functions.delete_file(path)

            track.delete()
        else:
            return "You can't delete an accepted track"
    else:
        return "This track is not yours"
