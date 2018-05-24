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
    url(r'^acceptTrack/(?P<track_id>\d+)', views.accept_track,
        name='acceptTrack'),
    url(r'^becomePremium/(?P<username>\w+)', views.become_premium,
        name='becomePremium'),
    url(r'^createAccount', views.create_account, name='createAccount'),
    url(r'^createInstrument', views.create_instrument, name='createInstrument'),
    url(r'^createSong', views.create_song, name='createSong'),
    url(r'^deleteInstrument/(?P<instrument_id>\d+)', views.delete_instrument,
        name='deleteInstrument'),
    url(r'^deleteSong/(?P<song_id>\d+)', views.delete_song, name='deleteSong'),
    url(r'^deleteTrack/(?P<track_id>\d+)', views.delete_track,
        name='deleteTrack'),
    url(r'^denyTrack/(?P<track_id>\d+)', views.deny_track, name='denyTrack'),
    url(r'^downloadTrack/(?P<track_id>\d+)', views.download_track,
        name='downloadTrack'),
    url(r'^editInstrument/(?P<instrument_id>\d+)', views.edit_instrument,
        name='editInstrument'),
    url(r'^finishSong/(?P<song_id>\d+)', views.finish_song, name='finishSong'),
    url(r'^getPremium', views.get_premium, name='getPremium'),
    url(r'^index', views.index, name='index'),
    url(r'^instruments', views.instruments, name='instruments'),
    url(r'^login', views.login_user, name='login'),
    url(r'^logout', views.logout_user, name='logout'),
    url(r'^mySongs', views.my_songs, name='mySongs'),
    url(r'^myTracks', views.my_tracks, name='myTracks'),
    url(r'^musicians', views.musicians, name='musicians'),
    url(r'^profile/(?P<musician_username>\w+)', views.profile, name='profile'),
    url(r'^publishSong/(?P<song_id>\d+)', views.publish_song,
        name='publishSong'),
    url(r'^reopenSong/(?P<song_id>\d+)', views.reopen_song, name='reopenSong'),
    url(r'^songs', views.songs, name='songs'),
    url(r'^song/(?P<song_id>\d+)', views.song_info, name='songInfo'),
    url(r'^tracks/(?P<song_id>\d+)', views.tracks, name='tracks'),
    url(r'^uploadTrack/(?P<song_id>\d+)', views.upload_track,
        name='uploadTrack'),
]
