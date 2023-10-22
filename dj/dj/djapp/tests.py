from django.test import TestCase, Client
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status


class UserModelTestCase(TestCase):
    usname = '0nam'
    uspwd = '0pwd'

    def setUp(self):
        # pass
        User.objects.create(username=self.usname, password=make_password(self.uspwd))
    def test_model_user_c(self):
        print('Testing Creating User')
        user = User.objects.get(username=self.usname)
        self.assertEqual(user.username, self.usname)

class NewsListTestCase(TestCase):
    def setUp(self):
        pass
    def test_view_news(self):
        print('Testing Request To News')
        client = Client()
        myresponse = client.get(reverse('news'))
        myjson = myresponse.json()
        self.assertEqual(myresponse.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(myjson)
        self.assertIn("{'news': ", str(myjson))
