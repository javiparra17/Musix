from main.models import Musician
from main.forms import MusicianForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect


def create_account(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('index.html')
    if request.method == 'POST':
        form = MusicianForm(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password2']:
                user = User.objects.create_user(form.cleaned_data['username'],
                                                form.cleaned_data['email'],
                                                form.cleaned_data['password'])
                user.first_name = form.cleaned_data['name']
                user.last_name = form.cleaned_data['surname']

                gender = form.cleaned_data['gender']
                description = form.cleaned_data['description']
                country = form.cleaned_data['country']
                photo = form.cleaned_data['photo']
                city = form.cleaned_data['city']
                Musician.objects.create(user=user, gender=gender,
                                        description=description,
                                        country=country, photo=photo, city=city)

                return HttpResponseRedirect('index.html')
            else:
                error = "The passwords are not the same"
                return render(request, 'createAccount.html',
                              {'form': form, 'error': error})
    else:
        form = MusicianForm()

    return render(request, 'createAccount.html', {'form': form})
