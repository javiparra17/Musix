from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from main.forms import *
from main.models import *
import main.functions as functions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
import os

def index(request):
    return render(request, "index.html")

# USER AND MUSICIAN
# Views of login, create account, edit profiles and list users

def createAccount(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('index.html')
    if request.method == 'POST':
        form = MusicianForm(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password2']:
                user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
                user.first_name = form.cleaned_data['name']
                user.last_name = form.cleaned_data['surname']
                Musician.objects.create(user=user, gender=form.cleaned_data['gender'], description=form.cleaned_data['description'],
                                        country=form.cleaned_data['country'], photo=form.cleaned_data['photo'], city=form.cleaned_data['city'])
                return HttpResponseRedirect('index.html')
            else:
                error = "The passwords are not the same"
                return render(request, 'createAccount.html', {'form': form, 'error': error})
    else:
        form = MusicianForm()

    return render(request, 'createAccount.html', {'form':form})

def loginUser(request):
    if not request.user:
        return HttpResponseRedirect('/index')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_views.login(request, user)
                return HttpResponseRedirect('/index')
            else:
                error = "Incorrect user or password"
                return render(request, 'login.html', {'form': form}, {'error': error})
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

#@login_required(login_url='/login.html')
def logoutUser(request):
    auth_views.logout(request)
    return HttpResponseRedirect('/index')

def musicians(request):
    musicians = Musician.objects.all()
    return render(request, 'musicians.html', {'musicians': musicians})

# SONG
# Views to create, list and edit songs

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

# TRACK
# Views to upload tracks, accept and deny tracks, and list tracks for a song

#@login_required(login_url='/login.html')
def uploadTrack(request):
    if request.method == 'POST':
        form = TrackForm(request.POST, request.FILES)
        if form.is_valid():
            Track.objects.create(instrument=form.cleaned_data['instrument'], sound=form.cleaned_data['sound'])
            return redirect('index.html')
    else:
        form = TrackForm()

    return render(request, 'uploadTrack.html', {'form':form})

#@login_required(login_url='/login.html')
def listTracks(request, songId):
    song = Song.objects.filter(id=songId)
    tracks = Track.objects.filter(song=song)

    return render(request, 'tracks.html', {'tracks': tracks})

#@login_required(login_url='/login.html')
def acceptTrack(request, trackId):
    track = Track.objects.filter(id=trackId)

    if track.status == 'P':
        track.status = 'A'
        track.save()

    return HttpResponseRedirect('/tracks')


# @login_required(login_url='/login.html')
def denyTrack(request, trackId):
    track = Track.objects.filter(id=trackId)

    if track.status == 'P':
        track.status = 'D'
        track.save()

    return HttpResponseRedirect('/tracks')

# INSTRUMENT
# Views to create, edit and delete instruments

@login_required(login_url='/login.html')
def createInstrument(request):
    if request.method == 'POST':
        form = InstrumentForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            image = form.cleaned_data['image']

            checkInstrument = Instrument.objects.filter(name=name)
            if len(checkInstrument) == 0:
                Instrument.objects.create(name=name, image=image)
                return redirect('/instruments')
            else:
                error = "This instrument already exists"
                return render(request, 'createInstrument.html', {'form': form, 'error': error})
    else:
        form = InstrumentForm()
    return render(request, 'createInstrument.html', {'form':form})

@login_required(login_url='/login.html')
def instruments(request):
    instruments = Instrument.objects.all()

    return render(request, 'instruments.html', {'instruments': instruments})

@login_required(login_url='/login.html')
def editInstrument(request, instrumentId):
    instrument = Instrument.objects.get(id=instrumentId)
    if request.method == "POST":
        form = InstrumentForm(request.POST, request.FILES)
        if form.is_valid():
            path = "/static/media/" + str(instrument.image)
            functions.deleteFile(path)

            instrument.name = form.cleaned_data['name']
            instrument.image = form.cleaned_data['image']

            instrument.save()
            return HttpResponseRedirect('/instruments')
    else:
        form = InstrumentForm(instance=instrument)
    return render(request, "editInstrument.html", {'form': form, 'instrument': instrument})

@login_required(login_url='/login.html')
def deleteInstrument(request, instrumentId):
    instrument = Instrument.objects.get(id=instrumentId)

    image = instrument.image
    path = "/static/media/" + str(image)
    functions.deleteFile(path)

    instrument.delete()

    return HttpResponseRedirect('/instruments')