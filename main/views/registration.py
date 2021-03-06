from main.models import Musician
from main.forms import MusicianForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from time import gmtime, strftime


def create_account(request):
    if not request.user.is_anonymous():
        raise PermissionDenied
    if request.method == 'POST':
        form = MusicianForm(request.POST, request.FILES)
        if form.is_valid():
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['password2']

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            exist_username = User.objects.filter(username=username)
            exist_email = User.objects.filter(email=email)

            if len(exist_username) is 0:

                if len(exist_email) is 0:

                    if password == confirm_password:
                        user = User.objects.create_user(username=username,
                                                        email=email,
                                                        password=password)
                        name = form.cleaned_data['name']
                        surname = form.cleaned_data['surname']
                        user.first_name = name
                        user.last_name = surname

                        user.save()

                        phone = form.cleaned_data['phone']
                        photo = form.cleaned_data['photo']

                        registration_date = strftime("%Y-%m-%d", gmtime())

                        Musician.objects.create(user=user, phone=phone,
                                                photo=photo,
                                                registrationDate=registration_date)

                        return HttpResponseRedirect('index.html')

                    else:
                        error = "The passwords are not the same"
                        return render(request, 'createAccount.html',
                                      {'form': form, 'error': error})

                else:
                    error = "This email already exists. " \
                            "Choose another one, please"
                    return render(request, 'createAccount.html',
                                  {'form': form, 'error': error})

            else:
                error = "This username already exists. " \
                        "Choose another one, please"
                return render(request, 'createAccount.html',
                              {'form': form, 'error': error})

    else:
        form = MusicianForm()

    return render(request, 'createAccount.html', {'form': form})
