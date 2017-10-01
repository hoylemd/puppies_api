from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient


class UserListTest(TestCase):
    def setUp(self):
        self.url = reverse('user-list')
        self.client = APIClient()

        self.administrator = get_user_model().objects.create(
            username='admin',
            is_staff=True,
            is_superuser=True,
        )
        self.administrator.set_password('secret123')
        self.administrator.save()

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

    def test_list_users__unauthenticated(self):
        """Should return 403 unauthenticated"""
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 403)

    def test_list_users__as_admin(self):
        """Should return the list of users"""
        mustang = get_user_model().objects.create(
            username='mustang',
            password='L172363',
        )
        sevro = get_user_model().objects.create(
            username='goblin',
            password='i_am_ares',
        )

        self.client.login(username='admin',
                          password='secret123')
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertIn(sevro.username, response.content)
        self.assertIn(mustang.username, response.content)
        self.assertIn(self.administrator.username, response.content)


class UserDetailsTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.administrator = get_user_model().objects.create(
            username='admin',
            is_staff=True,
            is_superuser=True,
        )
        self.administrator.set_password('secret123')
        self.administrator.save()

        self.url = reverse('user-detail', kwargs={'pk': self.administrator.id})

    def test_update_name(self):
        """Should allow users to change their first and last name"""
        self.client.login(username='admin', password='secret123')

        data = {
            'first_name': 'Fitchner',
            'last_name': 'au Barca',
        }

        response = self.client.patch(self.url, data)

        self.assertEqual(response.status_code, 200)
        self.assertIn('admin', response.content)
        self.administrator.refresh_from_db()
        self.assertEqual(self.administrator.first_name, 'Fitchner')
        self.assertEqual(self.administrator.last_name, 'au Barca')
