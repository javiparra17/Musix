from main.models import Instrument
from main.forms import InstrumentForm
from main.services import instrument as service
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login.html')
def create_instrument(request):
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
    all_instruments = Instrument.objects.all()

    return render(request, 'instruments.html', {'instruments': all_instruments})


@login_required(login_url='/login.html')
def edit_instrument(request, instrument_id):
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
    instrument = Instrument.objects.get(id=instrument_id)

    service.delete_instrument(instrument)

    return HttpResponseRedirect('/instruments')
