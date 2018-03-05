from django.shortcuts import render, redirect
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "index.html")

def createAccount(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index.html')
    else:
        form = UserForm()

    return render(request, 'createAccount.html', {'form':form })

#@login_required(login_url='/login.html')
def createSong(request):
    if request.method == 'POST':
        form = CreateSongForm(request.POST)
        if form.is_valid():
            print form.requiredInstruments
            preSong = form.save(commit=False)
            preSong.user = request.user
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
            form.save()
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