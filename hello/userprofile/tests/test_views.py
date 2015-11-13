from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client
from django.test.client import RequestFactory


class ViewUserTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        self.user = User.objects.create_user('john', 'lennon@gmail.com', '111111')

    def test_access_user_list(self):
        # non-login users will be redirect to login page
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 302)

    def test_login_user(self):
        self.client.login(username='john', password='111111')
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)

    def test_blank_page(self):
        self.client.login(username='john', password='111111')
        response = self.client.get('/users/?page=4000')
        self.assertEqual(response.status_code, 200)


class ViewSearchTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('john', 'lennon@gmail.com', '111111')

    def test_access_user_list_non_login(self):
        # non-login users will be redirect to login page
        response = self.client.get('/users/search/')
        self.assertEqual(response.status_code, 302)

    def test_access_user_list_login(self):
        # list all users when get request without search keyword
        self.client.login(username='john', password='111111')
        response = self.client.get('/users/search/')
        self.assertEqual(response.status_code, 200)

    def test_search_with_search_keyword(self):
        User.objects.create_user('adam', 'adam@gmail.com', '111111')
        self.client.login(username='john', password='111111')
        # make sure server will response user Adam when client search with keyword adam
        response = self.client.get('/users/search/?s=adam')
        self.assertContains(response, 'adam')
        # john will not be displayed in searching list with adam keyword
        self.assertNotContains(response, 'john')
        self.assertEqual(response.status_code, 200)
