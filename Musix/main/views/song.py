from main.models import Song, Musician, Track
from main.forms import SongForm
from main.services import song as service
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login.html')
def create_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            author = form.cleaned_data['author']
            description = form.cleaned_data['description']
            required_instruments = form.cleaned_data['requiredInstruments']
            additional_instruments = form.cleaned_data['additionalInstruments']
            user = request.user
            creator = Musician.objects.get(user=user)

            service.create_song(name, author, description, required_instruments,
                                additional_instruments, creator)

            return redirect('mySongs.html')
    else:
        form = SongForm()

    return render(request, 'createSong.html', {'form': form})


@login_required(login_url='/login.html')
def my_songs(request):
    user = request.user
    musician = Musician.objects.get(user=user)
    all_songs = service.my_songs(musician)

    return render(request, 'mySongs.html', {'songs': all_songs})


@login_required(login_url='/login.html')
def finish_song(request, song_id):
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
def delete_song(request, song_id):
    song = Song.objects.get(id=song_id)
    musician = Musician.objects.get(user=request.user)
    tracks = Track.objects.filter(song=song)

    if song.creator == musician:
        if len(tracks) == 0:
            song.delete()
        else:
            error = "You can't delete a song with tracks"
            return render(request, 'mySongs.html', {'error': error})
    else:
        error = "This song is not yours"
        return render(request, 'mySongs.html', {'error': error})

    return HttpResponseRedirect('/mySongs')


def songs(request):
    user = request.user.is_authenticated()
    if user:
        logged = True
    else:
        logged = False

    all_songs = service.songs(logged)

    return render(request, 'songs.html', {'songs': all_songs})


def song_info(request, song_id):
    song = Song.objects.get(id=song_id)
    required_instruments = song.requiredInstruments.all()

    return render(request, 'song.html', {'song': song, 'required_instruments':
        required_instruments})
