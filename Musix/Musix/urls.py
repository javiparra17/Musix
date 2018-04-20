"""Musix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from main import views

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^index', views.index, name='index'),
    url(r'^finishSong/(?P<songId>\d+)', views.finishSong, name='finishSong'),
    url(r'^createAccount', views.createAccount, name='createAccount'),
    url(r'^createInstrument', views.createInstrument, name='createInstrument'),
    url(r'^createSong', views.createSong, name='createSong'),
    url(r'^deleteInstrument/(?P<instrumentId>\d+)', views.deleteInstrument, name='deleteInstrument'),
    url(r'^deleteSong/(?P<songId>\d+)', views.deleteSong, name='deleteSong'),
    url(r'^editInstrument/(?P<instrumentId>\d+)', views.editInstrument, name='editInstrument'),
    url(r'^instruments', views.listInstruments, name='instruments'),
    url(r'^login', views.loginUser, name='login'),
    url(r'^logout', views.logoutUser, name='logout'),
    url(r'^mySongs', views.mySongs, name='mySongs'),
    url(r'^reopenSong/(?P<songId>\d+)', views.reopenSong, name='reopenSong'),
    url(r'^uploadTrack', views.uploadTrack, name='uploadTrack'),
]
