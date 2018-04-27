from main.models import Instrument
from main.forms import InstrumentForm
import main.functions as functions
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login.html')
def createInstrument(request):
    if request.method == 'POST':
        form = InstrumentForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            image = form.cleaned_data['image']

            checkInstrument = Instrument.objects.filter(name=name)
            if len(checkInstrument) == 0:
                Instrument.objects.create(name=name, image=image)
                return redirect('/instruments')
            else:
                error = "This instrument already exists"
                return render(request, 'createInstrument.html', {'form': form, 'error': error})
    else:
        form = InstrumentForm()
    return render(request, 'createInstrument.html', {'form':form})

@login_required(login_url='/login.html')
def instruments(request):
    instruments = Instrument.objects.all()

    return render(request, 'instruments.html', {'instruments': instruments})

@login_required(login_url='/login.html')
def editInstrument(request, instrumentId):
    instrument = Instrument.objects.get(id=instrumentId)
    if request.method == "POST":
        form = InstrumentForm(request.POST, request.FILES)
        if form.is_valid():
            path = "/static/media/" + str(instrument.image)
            functions.deleteFile(path)

            instrument.name = form.cleaned_data['name']
            instrument.image = form.cleaned_data['image']

            instrument.save()
            return HttpResponseRedirect('/instruments')
    else:
        form = InstrumentForm(instance=instrument)
    return render(request, "editInstrument.html", {'form': form, 'instrument': instrument})

@login_required(login_url='/login.html')
def deleteInstrument(request, instrumentId):
    instrument = Instrument.objects.get(id=instrumentId)

    image = instrument.image
    path = "/static/media/" + str(image)
    functions.deleteFile(path)

    instrument.delete()

    return HttpResponseRedirect('/instruments')