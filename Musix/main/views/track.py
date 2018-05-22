from main.models import Track, Song, Instrument
from main.forms import TrackForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from main.services import track as service
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied


@login_required(login_url='/login.html')
def upload_track(request, song_id):
    try:
        musician = request.user.musician
    except ObjectDoesNotExist:
        raise PermissionDenied
    
    song = Song.objects.get(id=song_id)
    if song.additionalInstruments:
        instruments = Instrument.objects.all()
    else:
        instruments = song.requiredInstruments.all()

    if request.method == 'POST':
        form = TrackForm(request.POST, request.FILES)
        if form.is_valid():
            instrument = form.cleaned_data['instrument']
            sound = form.cleaned_data['sound']

            service.upload_track(instrument, sound, musician, song)
            return redirect('myTracks.html')
    else:
        form = TrackForm()

    return render(request, 'uploadTrack.html', {'form': form, 'song': song,
                                                'instruments': instruments})


@login_required(login_url='/login.html')
def my_tracks(request):
    try:
        musician = request.user.musician
    except ObjectDoesNotExist:
        raise PermissionDenied

    mytracks = service.my_tracks(musician)

    return render(request, 'myTracks.html', {'tracks': mytracks})


@login_required(login_url='/login.html')
def tracks(request, song_id):
    try:
        musician = request.user.musician
    except ObjectDoesNotExist:
        raise PermissionDenied

    if not musician.premium:
        raise PermissionDenied

    song = Song.objects.get(id=song_id)
    song_tracks = service.tracks(song)

    song_tracksAP = song_tracks.exclude(status="D")

    tracks_ids = []
    for t in song_tracksAP:
        tracks_ids.append(t.id)

    return render(request, 'tracks.html', {'tracks': song_tracks, 'song': song,
                                           'tracks_ids': tracks_ids})


@login_required(login_url='/login.html')
def accept_track(request, track_id):
    try:
        musician = request.user.musician
    except ObjectDoesNotExist:
        raise PermissionDenied

    if not musician.premium:
        raise PermissionDenied

    track = Track.objects.get(id=track_id)

    service.accept_track(track)

    return HttpResponseRedirect('/tracks/' + str(track.song.id))


@login_required(login_url='/login.html')
def deny_track(request, track_id):
    try:
        musician = request.user.musician
    except ObjectDoesNotExist:
        raise PermissionDenied

    if not musician.premium:
        raise PermissionDenied

    track = Track.objects.get(id=track_id)

    service.deny_track(track)

    return HttpResponseRedirect('/tracks/' + str(track.song.id))
