from main.models import Report


def create_report(description, affected, reported):
    report = Report.objects.create(description=description,
                                   affected=affected, reported=reported)
    return report


def reports():
    return Report.objects.all()


def process_report(report):
    if not report.processed:
        report.processed = True
        report.save()
    else:
        return "This report is already processed"
    return report


def delete_report(report):
    if report.processed:
        report.delete()
    else:
        return "You can not delete an unprocessed report"
