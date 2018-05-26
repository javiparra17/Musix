from main.models import Musician, Track, Song
from main.forms import ProfileEditForm
from main.services import profile as service
import main.choices as choices
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied

COUNTRIES = choices.COUNTRIES


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


@login_required(login_url='/login.html')
def edit_profile(request, musician_username):
    try:
        musician = request.user.musician
    except ObjectDoesNotExist:
        raise PermissionDenied

    user = User.objects.get(username=musician_username)
    musician2 = Musician.objects.get(user=user)

    if musician != musician2:
        raise PermissionDenied

    if request.method == "POST":
        form = ProfileEditForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            username = form.cleaned_data['username']

            description = form.cleaned_data['description']
            photo = form.cleaned_data['photo']
            phone = form.cleaned_data['phone']
            gender = form.cleaned_data['gender']
            country = form.cleaned_data['country']
            city = form.cleaned_data['city']

            service.edit_profile(musician2, name, surname, username,
                                 description, photo, phone, gender, country,
                                 city)

            return HttpResponseRedirect('/profile/'+str(musician.user.username))
    else:
        form = ProfileEditForm(instance=musician2)

    return render(request, "editProfile.html",
                  {'form': form, 'musician': musician2, 'countries': COUNTRIES})
