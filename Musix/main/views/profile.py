from main.models import Musician, Track, Song
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User


def profile(request, musician_username):
    user = get_object_or_404(User, username=musician_username)
    musician = get_object_or_404(Musician, user=user)

    tracks = Track.objects.filter(musician=musician, status="A")
    finished_songs = Song.objects.filter(finished=True)
    accepted_tracks = []
    for t in tracks:
        if t.song in finished_songs:
            accepted_tracks.append(t)

    return render(request, 'profile.html', {'musician': musician,
                                            'tracks': accepted_tracks})
