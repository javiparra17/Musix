from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from main.forms import *
from main.models import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

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
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('index.html')
        else:
            error = "Incorrect user or password"
            return render(request, 'login.html', {'form': form}, {'error': error})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

#@login_required(login_url='/login.html')
def logoutUser(request):
    logout(request)
    return render(request, 'index.html', {'auth': False})

def listMusicians(request):
    musicians = Musician.objects.all()
    return render(request, 'musicians.html', {'musicians': musicians})

# SONG
# Views to create, list and edit songs

#@login_required(login_url='/login.html')
def createSong(request):
    if request.method == 'POST':
        form = CreateSongForm(request.POST)
        if form.is_valid():
            #creator = request.user
            requiredInstruments = functions.splitInstruments(form.cleaned_data['requiredInstruments'])
            Song.objects.create(name=form.cleaned_data['name'], author=form.cleaned_data['author'],
                                description=form.cleaned_data['description'], requiredInstruments=requiredInstruments,
                                additionalInstruments=form.cleaned_data['additionalInstruments'], finished=False)
            return redirect('index.html')
    else:
        form = CreateSongForm()

    return render(request, 'createSong.html', {'form':form })

#@login_required(login_url='/login.html')
def mySongs(request):
    user = request.user
    musician = Musician.objects.filter(user=user)
    songs = Song.objects.filter(creator=musician)

    return render(request, 'mySongs.html', {'songs': songs})

#@login_required(login_url='/login.html')
def closeSong(request, songId):
    song = Song.objects.filter(id=songId)

    if song.finished == False:
        song.finished = True
        song.save()
    return HttpResponseRedirect('/mySongs')

#@login_required(login_url='/login.html')
def reopenSong(request, songId):
    song = Song.objects.filter(id=songId)

    if song.finished == True:
        song.finished = False
        song.save()
    return HttpResponseRedirect('/mySongs')

def listSongs(request):
    songs = Song.objects.filter(finished=True)
    return render(request, 'songs.html', {'songs': songs})

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