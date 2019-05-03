# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from .views import index
from django.contrib.auth.models import User
import factory


from rest_framework.test import APITestCase



class UserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = User

    email = 'admin@admin.com'
    username = 'admin'
    password = 'admin'
    is_superuser = True
    is_staff = True
    is_active = True

class TestCalls(TestCase):
    def test_index_view(self):
        response = self.client.get('/index', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        self.client.login(username='admin', password='admin')  
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

