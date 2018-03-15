from django.shortcuts import render, redirect
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from forms import *
from models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

def index(request):
    return render(request, "index.html")

def createAccount(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('index.html')
    if request.method == 'POST':
        form = MusicianForm(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password2']:
                user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
                user.first_name = form.cleaned_data['name']
                user.last_name = form.cleaned_data['surname']
                Musician.objects.create(user=user, gender=form.cleaned_data['gender'], description=form.cleaned_data['description'],
                                        country=form.cleaned_data['country'], photo=form.cleaned_data['photo'], city=form.cleaned_data['city'])
                return HttpResponseRedirect('index.html')
            else:
                error = "The passwords are not the same"
                return render_to_response('createAccount.html', {'form': form, 'error': error})
    else:
        form = MusicianForm()

    return render_to_response('createAccount.html', {'form':form})

#@login_required(login_url='/login.html')
def createSong(request):
    if request.method == 'POST':
        form = CreateSongForm(request.POST)
        if form.is_valid():
            preSong = form.save(commit=False)
            preSong.requiredInstruments = functions.splitInstruments(preSong.requiredInstruments)
            preSong.finished = False
            #preSong.user = request.user
            preSong.save()
            return redirect('index.html')
    else:
        form = CreateSongForm()

    return render(request, 'createSong.html', {'form':form })

#@login_required(login_url='/login.html')
def uploadTrack(request):
    if request.method == 'POST':
        form = TrackForm(request.POST, request.FILES)
        if form.is_valid():
            preTrack = form.save(commit=False)
            preTrack.save()
            return redirect('index.html')
    else:
        form = TrackForm()

    return render(request, 'uploadTrack.html', {'form':form })

def loginUser(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return render(request, '/index.html')
            #else:
                # Return an 'invalid login' error message.
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form':form })

from django.contrib.auth import logout

def logout_view(request):
    logout(request)