#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated, changes may be lost if you
# go and generate it again. It was generated with the following command:
# ./manage.py dumpscript auth

import datetime

def run():

    from django.contrib.auth.models import User

    auth_user_1 = User()
    auth_user_1.username = u'admin'
    auth_user_1.first_name = u''
    auth_user_1.last_name = u''
    auth_user_1.email = u''
    auth_user_1.password = u'sha1$a3dbb$c356793168ecbe680fdd0cce1981480b05408104'
    auth_user_1.is_staff = True
    auth_user_1.is_active = True
    auth_user_1.is_superuser = True
    auth_user_1.last_login = datetime.datetime(2009, 1, 26, 14, 33, 17)
    auth_user_1.date_joined = datetime.datetime(2009, 1, 26, 14, 33)
    auth_user_1.save()

    auth_user_2 = User()
    auth_user_2.username = u'user'
    auth_user_2.first_name = u''
    auth_user_2.last_name = u''
    auth_user_2.email = u''
    auth_user_2.password = u'sha1$52c3c$cf2635fa24766e2d485a5ebee4c9c46f5c829ec9'
    auth_user_2.is_staff = False
    auth_user_2.is_active = True
    auth_user_2.is_superuser = False
    auth_user_2.last_login = datetime.datetime(2009, 1, 26, 14, 33, 46)
    auth_user_2.date_joined = datetime.datetime(2009, 1, 26, 14, 33, 46)
    auth_user_2.save()

    from django.contrib.sites.models import Site

    django_site_1 = Site()
    django_site_1.domain = u'localhost:8000'
    django_site_1.name = u'Development Server'
    django_site_1.save()


