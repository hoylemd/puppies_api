from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient


class UserListTest(TestCase):
    def setUp(self):
        self.url = reverse('user-list')
        self.client = APIClient()

    def test_create_user(self):
        """Should create a new user record unauthenticated"""
        data = {
            'username': 'reaper_of_mars',
            'email': 'reaper@marsinstitute.com',
            'password': 'secret123',
            'first_name': 'Darrow',
            'last_name': 'au Andromedus',
        }
        response = self.client.post(reverse('register'), data)

        self.assertEqual(response.status_code, 201)
        self.assertNotIn('password', response.data)

        sut = get_user_model().objects.get(username=data['username'])
        self.assertEqual(sut.email, data['email'])

        # check password
        self.assertFalse(self.client.login(username=data['username'],
                                           password='nope'))
        self.assertTrue(self.client.login(username=data['username'],
                                          password=data['password']))
