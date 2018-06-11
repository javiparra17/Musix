from main.models import Instrument, Administrator
from main.forms import InstrumentForm
from main.services import instrument as service
import main.functions as functions
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required(login_url='/login.html')
def create_instrument(request):
    try:
        Administrator.objects.get(user=request.user)
    except ObjectDoesNotExist:
        raise PermissionDenied

    if request.method == 'POST':
        form = InstrumentForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            image = form.cleaned_data['image']

            check_instrument = Instrument.objects.filter(name=name)
            if len(check_instrument) == 0:
                service.create_instrument(name, image)
                return redirect('/instruments')
            else:
                error = "This instrument already exists"
                return render(request, 'createInstrument.html',
                              {'form': form, 'error': error})
    else:
        form = InstrumentForm()
    return render(request, 'createInstrument.html', {'form': form})


@login_required(login_url='/login.html')
def instruments(request):
    try:
        Administrator.objects.get(user=request.user)
    except ObjectDoesNotExist:
        raise PermissionDenied

    all_instruments = service.instruments()
    used_instruments = functions.get_all_used_instruments()

    page_instruments = request.GET.get("page", 1)
    paginator_instruments = Paginator(all_instruments, 7)

    try:
        p_instruments = paginator_instruments.page(page_instruments)
    except (PageNotAnInteger, EmptyPage):
        p_instruments = paginator_instruments.page(1)

    return render(request, 'instruments.html', {'instruments': p_instruments,
                                                'used_instruments':
                                                    used_instruments})


@login_required(login_url='/login.html')
def edit_instrument(request, instrument_id):
    try:
        Administrator.objects.get(user=request.user)
    except ObjectDoesNotExist:
        raise PermissionDenied

    instrument = Instrument.objects.get(id=instrument_id)
    if request.method == "POST":
        form = InstrumentForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            image = form.cleaned_data['image']

            service.edit_instrument(instrument, name, image)

            return HttpResponseRedirect('/instruments')
    else:
        form = InstrumentForm(instance=instrument)
    return render(request, "editInstrument.html",
                  {'form': form, 'instrument': instrument})


@login_required(login_url='/login.html')
def delete_instrument(request, instrument_id):
    try:
        Administrator.objects.get(user=request.user)
    except ObjectDoesNotExist:
        raise PermissionDenied

    instrument = Instrument.objects.get(id=instrument_id)

    used_instruments = functions.get_all_used_instruments()

    if instrument not in used_instruments:
        service.delete_instrument(instrument)

        return HttpResponseRedirect('/instruments')
    else:
        error = "You can not delete an used instrument"
        return render(request, "instruments.html", {'error': error})
