from models import *
from datetime import datetime
import django.core.management as djangocmd
from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_date
from django.utils.dateparse import parse_time

path = "populateFolder"

class Command(BaseCommand):
    args = 'none'
    help = 'Populate the database'

    def _populate(self):
        admin_user = User.objects.create_user(email='admin@musix.com',
                                              username='admin',
                                              password='admin')
        admin_user.save()
        admin = Administrator(user=admin_user)
        admin.save()

        userM1 = User.objects.create_user(first_name='musician1Name',
                                         last_name='musician1Surname',
                                         email='musician1@musix.com',
                                         username='musician1',
                                         password='musician1')
        userM1.save()
        musician1 = Musician(user=userM1,
                             gender='M',
                             description="Description1",
                             country='ES',
                             city='City1',
                             registrationDate=parse_date('2017-07-15'),
                             premium=False)
        musician1.save()

    def handle(self, *args, **options):
        djangocmd.call_command('flush', interactive=False)
        djangocmd.call_command('migrate')
        print "Populating database..."
        self._populate()
