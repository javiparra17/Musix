from main.models import Musician, Administrator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from main.services import ban as service


@login_required(login_url='/login.html')
def ban(request, musician_id):
    try:
        Administrator.objects.get(user=request.user)
    except ObjectDoesNotExist:
        raise PermissionDenied

    musician = Musician.objects.get(id=musician_id)

    if not musician.banned:
        service.ban(musician)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/login.html')
def unban(request, musician_id):
    try:
        Administrator.objects.get(user=request.user)
    except ObjectDoesNotExist:
        raise PermissionDenied

    musician = Musician.objects.get(id=musician_id)

    if musician.banned:
        service.unban(musician)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
