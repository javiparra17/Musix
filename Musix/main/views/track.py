from main.models import Track, Song
from main.forms import TrackForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

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