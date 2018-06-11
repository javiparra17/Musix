from django.test import TestCase
from main.tests import test_user as setup
from main.services import report as service
from django.contrib.auth.models import User
from main.models import Musician, Report


class ReportTest(TestCase):
    def setUp(self):
        setup.set_up_musician_no_premium()
        setup.set_up_musician_premium()

    def test_create_report(self):
        user1 = User.objects.get(username="musician1")
        musician1 = Musician.objects.get(user=user1)

        user2 = User.objects.get(username="musician2")
        musician2 = Musician.objects.get(user=user2)

        description = "Description"

        report = service.create_report(description, musician1, musician2)

        report_saved = Report.objects.get(id=report.id)

        self.assertEquals(report_saved.description, description)
        self.assertEquals(report_saved.processed, False)

        return report

    def test_negative_process_report(self):
        report = self.test_create_report()
        report.processed = True
        report.save()

        result = service.process_report(report)

        self.assertEquals(result, "This report is already processed")

    def test_process_report(self):
        report = self.test_create_report()

        service.process_report(report)

        self.assertEquals(report.processed, True)

    def test_negative_delete_report(self):
        report = self.test_create_report()

        result = service.delete_report(report)

        self.assertEquals(result, "You can not delete an unprocessed report")

    def test_delete_report(self):
        report = self.test_create_report()
        report.processed = True
        report.save()

        service.delete_report(report)

        reports = Report.objects.all()

        self.assertFalse(report in reports)
