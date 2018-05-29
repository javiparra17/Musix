from django.shortcuts import render
from main.services import musician as service
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def musicians(request):
    try:
        musician = request.user.musician

        all_musicians = service.musicians(musician)
    except:
        all_musicians = service.musicians(None)

    page_musicians = request.GET.get("page", 1)
    paginator_musicians = Paginator(all_musicians, 7)

    try:
        p_musicians = paginator_musicians.page(page_musicians)
    except (PageNotAnInteger, EmptyPage):
        p_musicians = paginator_musicians.page(1)

    return render(request, 'musicians.html', {'musicians': p_musicians})
