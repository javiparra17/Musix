from main.models import Musician
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from main.services import premium as service


@login_required(login_url='/login.html')
def get_premium(request):
    try:
        musician = request.user.musician
    except ObjectDoesNotExist:
        raise PermissionDenied

    if musician.premium:
        raise PermissionDenied

    return render(request, "getPremium.html")


@login_required(login_url='/login.html')
def become_premium(request, username):
    try:
        musician = request.user.musician
    except ObjectDoesNotExist:
        raise PermissionDenied

    if musician.premium:
        raise PermissionDenied

    user = User.objects.get(username=username)
    musician = Musician.objects.get(user=user)

    service.become_premium(musician)

    return HttpResponseRedirect('/index')
