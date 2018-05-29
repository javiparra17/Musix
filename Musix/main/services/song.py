from main.models import Song, Track
import main.functions as functions


def create_song(name, author, tune, accidental, tonality, bpm, description, score,
                required_instruments, additional_instruments, creator):
    song = Song.objects.create(name=name, author=author, tune=tune,
                               accidental=accidental, tonality=tonality,
                               bpm=bpm, description=description, score=score,
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


def edit_song(song, name, author, tune, accidental, tonality, bpm, description,
              score, required_instruments, additional_instruments):
    song.name = name
    song.author = author
    song.tune = tune
    song.accidental = accidental
    song.tonality = tonality
    song.bpm = bpm
    song.description = description
    song.score = score
    song.requiredInstruments = required_instruments
    song.additionalInstruments = additional_instruments

    if not song.finished:
        song.save()
    else:
        return "You can not edit a finished song"

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
