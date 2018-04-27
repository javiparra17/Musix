from main.models import Song, Musician
from main.forms import SongForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

#@login_required(login_url='/login.html')
def createSong(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            #creator = request.user
            requiredInstruments = form.cleaned_data['requiredInstruments']
            Song.objects.create(name=form.cleaned_data['name'], author=form.cleaned_data['author'],
                                description=form.cleaned_data['description'], requiredInstruments=requiredInstruments,
                                additionalInstruments=form.cleaned_data['additionalInstruments'], finished=False)
            return redirect('index.html')
    else:
        form = SongForm()

    return render(request, 'createSong.html', {'form':form })

@login_required(login_url='/login.html')
def mySongs(request):
    user = request.user
    musician = Musician.objects.get(user=user)
    songs = Song.objects.filter(creator=musician)

    return render(request, 'mySongs.html', {'songs': songs})

@login_required(login_url='/login.html')
def finishSong(request, songId):
    song = Song.objects.get(id=songId)
    musician = Musician.objects.get(user=request.user)

    if song.creator == musician:
        if song.finished == False:
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
def reopenSong(request, songId):
    song = Song.objects.get(id=songId)
    musician = Musician.objects.get(user=request.user)

    if song.creator == musician:
        if song.finished == True:
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
def deleteSong(request, songId):
    song = Song.objects.get(id=songId)
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
        songs = Song.objects.all()
    else:
        songs = Song.objects.filter(finished=True)

    info = False

    return render(request, 'songs.html', {'songs': songs, 'info': info})

def songInfo(request, songId):
    song = Song.objects.get(id=songId)

    return render(request, 'song.html', {'song': song})