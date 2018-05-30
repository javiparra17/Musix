from main.models import Musician, Administrator, Report
from django.contrib.auth.models import User
from main.forms import ReportForm
from main.services import report as service
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required(login_url='/login.html')
def create_report(request, musician_username):
    try:
        affected = request.user.musician
    except ObjectDoesNotExist:
        raise PermissionDenied

    user_reported = User.objects.get(username=musician_username)
    reported = Musician.objects.get(user=user_reported)

    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            description = form.cleaned_data['description']

            service.create_report(description, affected, reported)

            return HttpResponseRedirect('/profile/' +
                                        str(reported.user.username))
    else:
        form = ReportForm()

    return render(request, 'createReport.html', {'form': form,
                                                 'reported': reported})


@login_required(login_url='/login.html')
def reports(request):
    try:
        Administrator.objects.get(user=request.user)
    except ObjectDoesNotExist:
        raise PermissionDenied

    all_reports = service.reports()

    page_reports = request.GET.get("page", 1)
    paginator_reports = Paginator(all_reports, 10)

    try:
        p_reports = paginator_reports.page(page_reports)
    except (PageNotAnInteger, EmptyPage):
        p_reports = paginator_reports.page(1)

    return render(request, 'reports.html', {'reports': p_reports})


@login_required(login_url='/login.html')
def process_report(request, report_id):
    try:
        Administrator.objects.get(user=request.user)
    except ObjectDoesNotExist:
        raise PermissionDenied

    report = Report.objects.get(id=report_id)

    if not report.processed:
        service.process_report(report)
        return HttpResponseRedirect('/reports/')


@login_required(login_url='/login.html')
def delete_report(request, report_id):
    try:
        Administrator.objects.get(user=request.user)
    except ObjectDoesNotExist:
        raise PermissionDenied

    report = Report.objects.get(id=report_id)

    if report.processed:
        service.delete_report(report)
        return HttpResponseRedirect('/reports/')
