from main.models import Track, Song, Instrument
from main.forms import TrackForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from main.services import track as service
import main.functions as functions
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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

            return redirect('/myTracks.html')
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

    page_mytracks = request.GET.get("page", 1)
    paginator_mytracks = Paginator(mytracks, 3)

    try:
        p_mytracks = paginator_mytracks.page(page_mytracks)
    except (PageNotAnInteger, EmptyPage):
        p_mytracks = paginator_mytracks.page(1)

    return render(request, 'myTracks.html', {'tracks': p_mytracks})


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

    song_tracks_ap = song_tracks.exclude(status="D")

    tracks_ids = []
    for t in song_tracks_ap:
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


@login_required(login_url='/login.html')
def delete_track(request, track_id):
    try:
        musician = request.user.musician
    except ObjectDoesNotExist:
        raise PermissionDenied

    track = Track.objects.get(id=track_id)

    if track.musician == musician:
        if track.status == "P" or track.status == "D":
            service.delete_track(musician, track)
        else:
            error = "You can't delete an accepted track"
            return render(request, 'myTracks.html', {'error': error})

    else:
        error = "This track is not yours"
        return render(request, 'myTracks.html', {'error': error})

    return HttpResponseRedirect('/myTracks')


@login_required(login_url='/login.html')
def download_track(request, track_id):
    try:
        musician = request.user.musician
    except ObjectDoesNotExist:
        raise PermissionDenied

    if not musician.premium:
        raise PermissionDenied

    track = Track.objects.get(id=track_id)

    response = functions.download_track(str(track.sound))

    return response
