from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied


@login_required(login_url='/login.html')
def get_premium(request):
    try:
        musician = request.user.musician
    except ObjectDoesNotExist:
        raise PermissionDenied

    if musician.premium:
        raise PermissionDenied

    return render(request, "getPremium.html")


def index(request):
    return render(request, "index.html")
