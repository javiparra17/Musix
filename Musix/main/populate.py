# from django.contrib.auth.models import User
from main import models
# from django.utils.dateparse import parse_date
# import django.core.management as djangocmd

def populate():
    # admin_user = User.objects.create_user(email='admin@musix.com',
    #                                       username='admin',
    #                                       password='admin')
    # admin_user.save()
    # admin = models.Administrator(user=admin_user)
    # admin.save()

    # userM1 = User.objects.create_user(first_name='musician1Name',
    #                                  last_name='musician1Surname',
    #                                  email='musician1@musix.com',
    #                                  username='musician1',
    #                                  password='musician1')
    # userM1.save()
    # musician1 = models.Musician(user=userM1,
    #                      gender='M',
    #                      description="Description1",
    #                      country='ES',
    #                      city='City1',
    #                      registrationDate=parse_date('2017-07-15'),
    #                      premium=False)
    # musician1.save()

    instrument1 = models.Instrument.objects.create(name="Piano")
    instrument1.save()
    instrument2 = models.Instrument.objects.create(name="Drums")
    instrument2.save()
    instrument3 = models.Instrument.objects.create(name="Bass")
    instrument3.save()


# def handle(self, *args, **options):
#     # djangocmd.call_command('flush', interactive=False)
#     # djangocmd.call_command('migrate')
#     print "Populating database..."
#     self.populate()

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'Musix.settings'
populate()