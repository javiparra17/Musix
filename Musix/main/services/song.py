from main.models import Song, Track
import main.functions as functions


def create_song(name, author, description, required_instruments,
                additional_instruments, creator):
    song = Song.objects.create(name=name, author=author,
                               description=description,
                               additionalInstruments=additional_instruments,
                               finished=False, creator=creator)

    song.requiredInstruments = required_instruments
    song.save()

    return song


def my_songs(musician):
    mysongs = Song.objects.filter(creator=musician)

    return mysongs


def finish_song(musician, song):
    if song.creator == musician:
        if not song.finished:
            song.finished = True
            song.save()
        else:
            return "This song is already finished"
    else:
        return "You can't finish this song"


def reopen_song(musician, song):
    if song.creator == musician:
        if song.finished:
            song.finished = False
            song.save()
        else:
            return "This song is already opened"
    else:
        return "You can't reopen this song"


def publish_song(song, sound):
    song.finishedSong = sound
    song.save()

    return song


def delete_song(musician, song):
    tracks = Track.objects.filter(song=song)

    if song.creator == musician:
        if len(tracks) == 0:
            song.delete()
        else:
            if song.finished:
                tracks.filter(status='P')
                if tracks:
                    return "This song has pending tracks"
                else:
                    sound = song.finishedSong
                    path = "/static/media/" + str(sound)
                    functions.delete_file(path)
                    song.delete()
            else:
                return "You can't delete an open song with tracks"
    else:
        return "This song is not yours"


def songs(logged):
    if logged:
        all_songs = Song.objects.all()
    else:
        all_songs = Song.objects.filter(finished=True)

    return all_songs
