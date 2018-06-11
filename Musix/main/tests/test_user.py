from django.contrib.auth.models import User
from main.models import Musician, Administrator
from django.utils.dateparse import parse_date


def set_up_musician_no_premium():
    user1 = User.objects.create_user(first_name='name1',
                                     last_name=' surname1',
                                     email='musician1@hotmail.com',
                                     username='musician1',
                                     password='musician1')
    user1.save()
    musician1 = Musician(user=user1,
                         gender='M',
                         description="",
                         country='ES',
                         city='Madrid',
                         registrationDate=parse_date('2017-07-15'),
                         premium=False,
                         banned=False)
    musician1.save()


def set_up_musician_premium():
    user2 = User.objects.create_user(first_name='name2',
                                     last_name=' surname2',
                                     email='musician2@hotmail.com',
                                     username='musician2',
                                     password='musician2')
    user2.save()
    musician2 = Musician(user=user2,
                         gender='M',
                         description="",
                         country='ES',
                         city='Madrid',
                         registrationDate=parse_date('2017-07-15'),
                         premium=True,
                         banned=False)
    musician2.save()


def set_up_musician_banned():
    user3 = User.objects.create_user(first_name='name3',
                                     last_name=' surname3',
                                     email='musician3@hotmail.com',
                                     username='musician3',
                                     password='musician3')
    user3.save()
    musician3 = Musician(user=user3,
                         gender='M',
                         description="",
                         country='ES',
                         city='Madrid',
                         registrationDate=parse_date('2017-07-15'),
                         premium=False,
                         banned=True)
    musician3.save()


def set_up_admin():
    admin_user = User.objects.create_user(email='admin@musix.com',
                                          username='admin',
                                          password='admin')
    admin_user.save()
    admin = Administrator(user=admin_user)
    admin.save()
