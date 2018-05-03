from main.models import Song, Musician, Track
from main.forms import SongForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login.html')
def create_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            creator = request.user.musician
            name = form.cleaned_data['name']
            author = form.cleaned_data['author']
            description = form.cleaned_data['description']
            required_instruments = form.cleaned_data['requiredInstruments']
            additional_instruments = form.cleaned_data['additionalInstruments']
            Song.objects.create(name=name, author=author,
                                description=description,
                                requiredInstruments=required_instruments,
                                additionalInstruments=additional_instruments,
                                finished=False, creator=creator)
            return redirect('index.html')
    else:
        form = SongForm()

    return render(request, 'createSong.html', {'form': form})


@login_required(login_url='/login.html')
def my_songs(request):
    user = request.user
    musician = Musician.objects.get(user=user)
    all_songs = Song.objects.filter(creator=musician)

    return render(request, 'mySongs.html', {'songs': all_songs})


@login_required(login_url='/login.html')
def finish_song(request, song_id):
    song = Song.objects.get(id=song_id)
    musician = Musician.objects.get(user=request.user)

    if song.creator == musician:
        if not song.finished:
            song.finished = True
            song.save()
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
            song.finished = False
            song.save()
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
        error = "You can't reopen this song"
        return render(request, 'mySongs.html', {'error': error})

    return HttpResponseRedirect('/mySongs')


def songs(request):
    if request.user:
        all_songs = Song.objects.all()
    else:
        all_songs = Song.objects.filter(finished=True)

    info = False

    return render(request, 'songs.html', {'songs': all_songs, 'info': info})


def song_info(request, song_id):
    song = Song.objects.get(id=song_id)

    return render(request, 'song.html', {'song': song})
