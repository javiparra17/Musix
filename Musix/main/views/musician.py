from main.models import Musician
from django.contrib.auth.models import User
from main.forms import SearchMusicianForm
from main.services import musician as service
from django.db.models import Q
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def musicians(request):
    try:
        musician = request.user.musician

        all_musicians = service.musicians(musician)
    except:
        all_musicians = service.musicians(None)

    if request.method == 'POST':
        form = SearchMusicianForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            if text == "":
                found_musicians = all_musicians
            else:
                found_user = User.objects.filter(Q(first_name__icontains=text) |
                                                 Q(last_name__icontains=text) |
                                                 Q(username__icontains=text))
                found_user.exclude(username="admin")
                found_musicians = []
                for u in found_user:
                    if request.user.is_authenticated():
                        musician = request.user.musician
                        if not u.id == musician.user.id:
                            m = Musician.objects.get(user=u)
                            found_musicians.append(m)
                    else:
                        m = Musician.objects.get(user=u)
                        found_musicians.append(m)

            page_musicians = request.GET.get("page", 1)
            paginator_musicians = Paginator(found_musicians, 7)

            try:
                p_musicians = paginator_musicians.page(page_musicians)
            except (PageNotAnInteger, EmptyPage):
                p_musicians = paginator_musicians.page(1)

            return render(request, 'musicians.html',
                          {'form': form, 'musicians': p_musicians})
    else:
        form = SearchMusicianForm()

        page_musicians = request.GET.get("page", 1)
        paginator_musicians = Paginator(all_musicians, 7)

        try:
            p_musicians = paginator_musicians.page(page_musicians)
        except (PageNotAnInteger, EmptyPage):
            p_musicians = paginator_musicians.page(1)

        return render(request, 'musicians.html', {'form': form,
                                                  'musicians': p_musicians})
