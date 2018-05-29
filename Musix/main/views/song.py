from main.models import Song, Musician, Track, Instrument
from main.forms import SongForm, FinishedSongForm
from main.services import song as service
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied


#@login_required(login_url='/login.html')
def create_song(request):
    try:
        musician = request.user.musician
    except ObjectDoesNotExist:
        raise PermissionDenied

    if not musician.premium:
        raise PermissionDenied

    instruments = Instrument.objects.all()

    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            author = form.cleaned_data['author']
            tune = form.cleaned_data['tune']
            accidental = form.cleaned_data['accidental']
            tonality = form.cleaned_data['tonality']
            bpm = form.cleaned_data['bpm']
            description = form.cleaned_data['description']
            score = form.cleaned_data['score']
            required_instruments = form.cleaned_data['requiredInstruments']
            additional_instruments = form.cleaned_data['additionalInstruments']
            creator = musician

            service.create_song(name, author, tune, accidental, tonality, bpm,
                                description, score, required_instruments,
                                additional_instruments, creator)

            return redirect('mySongs.html')
    else:
        form = SongForm()

    return render(request, 'createSong.html', {'form': form,
                                               'instruments': instruments})


@login_required(login_url='/login.html')
def my_songs(request):
    try:
        musician = request.user.musician
    except ObjectDoesNotExist:
        raise PermissionDenied

    if not musician.premium:
        raise PermissionDenied

    user = request.user
    musician = Musician.objects.get(user=user)
    all_songs = service.my_songs(musician)

    return render(request, 'mySongs.html', {'songs': all_songs})


@login_required(login_url='/login.html')
def finish_song(request, song_id):
    try:
        musician = request.user.musician
    except ObjectDoesNotExist:
        raise PermissionDenied

    if not musician.premium:
        raise PermissionDenied

    song = Song.objects.get(id=song_id)
    musician = Musician.objects.get(user=request.user)

    if song.creator == musician:
        if not song.finished:
            service.finish_song(musician, song)
        else:
            error = "This song is already finished"
            return render(request, 'mySongs.html', {'error': error})
    else:
        error = "You can't finish this song"
        return render(request, 'mySongs.html', {'error': error})

    return HttpResponseRedirect('/mySongs')


@login_required(login_url='/login.html')
def reopen_song(request, song_id):
    try:
        musician = request.user.musician
    except ObjectDoesNotExist:
        raise PermissionDenied

    if not musician.premium:
        raise PermissionDenied

    song = Song.objects.get(id=song_id)
    musician = Musician.objects.get(user=request.user)

    if song.creator == musician:
        if song.finished:
            service.reopen_song(musician, song)
        else:
            error = "This song is already opened"
            return render(request, 'mySongs.html', {'error': error})
    else:
        error = "You can't reopen this song"
        return render(request, 'mySongs.html', {'error': error})

    return HttpResponseRedirect('/mySongs')


@login_required(login_url='/login.html')
def publish_song(request, song_id):
    try:
        musician = request.user.musician
    except ObjectDoesNotExist:
        raise PermissionDenied

    if not musician.premium:
        raise PermissionDenied

    song = Song.objects.get(id=song_id)

    if request.method == 'POST':
        form = FinishedSongForm(request.POST, request.FILES)
        if form.is_valid():
            finished_song = form.cleaned_data['finishedSong']
            service.publish_song(song, finished_song)
            return redirect('/song/' + str(song.id))
    else:
        form = FinishedSongForm()
    return render(request, 'publishSong.html', {'form': form, 'song': song})


@login_required(login_url='/login.html')
def delete_song(request, song_id):
    try:
        musician = request.user.musician
    except ObjectDoesNotExist:
        raise PermissionDenied

    if not musician.premium:
        raise PermissionDenied

    song = Song.objects.get(id=song_id)
    musician = Musician.objects.get(user=request.user)
    tracks = Track.objects.filter(song=song)
    songs = Song.objects.filter(creator=musician)

    if song.creator == musician:
        if len(tracks) == 0:
            song.delete()
        else:
            if song.finished:
                tracks.filter(status='P')
                if tracks:
                    error = "This song has pending tracks"
                    return render(request, 'mySongs.html', {'songs': songs,
                                                            'error': error})
                else:
                    service.delete_song(musician, song)
                    return redirect("/mySongs")
            else:
                error = "You can't delete an open song with tracks"
                return render(request, 'mySongs.html', {'songs': songs,
                                                        'error': error})

    else:
        error = "This song is not yours"
        return render(request, 'mySongs.html', {'songs': songs,
                                                'error': error})

    return HttpResponseRedirect('/mySongs')


def songs(request):
    user = request.user.is_authenticated()
    participations = []
    if user:
        logged = True
        tracks = Track.objects.filter(musician=request.user.musician)\
            .exclude(status="D")
        for t in tracks:
            participations.append(t.song)
    else:
        logged = False

    all_songs = service.songs(logged)

    return render(request, 'songs.html', {'songs': all_songs,
                                          'participations': participations})


def song_info(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    required_instruments = song.requiredInstruments.all()
    musician = song.creator

    try:
        user = request.user.musician
        tracks = Track.objects.filter(musician=user).exclude(status="D")
        participations = []
        for t in tracks:
            participations.append(t.song)
        return render(request, 'song.html',
                      {'song': song,
                       'required_instruments': required_instruments,
                       'musician': musician, 'participations': participations})
    except:
        return render(request, 'song.html',
                      {'song': song})
