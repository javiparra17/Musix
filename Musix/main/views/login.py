from main.forms import LoginForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import views as auth_views


def login_user(request):
    if not request.user:
        return HttpResponseRedirect('/index')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if not user.musician.banned:
                if user is not None:
                    auth_views.login(request, user)
                    return HttpResponseRedirect('/index')
                else:
                    error = "Incorrect user or password"
                    return render(request, 'login.html',
                                  {'form': form, 'error': error})
            else:
                error = "Your account have been banned"
                return render(request, 'login.html',
                              {'form': form, 'error': error})
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


@login_required(login_url='/login.html')
def logout_user(request):
    auth_views.logout(request)
    return HttpResponseRedirect('/index')
