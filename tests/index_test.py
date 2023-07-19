from django.test import TestCase

# Create your tests here.

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib import messages

from users.forms import CustomAuthenticationForm


class LoginViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('login')
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@test.com',
            'password': 'testpassword',
        }
        User = get_user_model()
        self.user = User.objects.create_user(**self.user_data)

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')
        form = response.context['form']
        self.assertIsInstance(form, CustomAuthenticationForm)

    def test_post_valid(self):
        response = self.client.post(self.url, self.user_data)
        self.assertRedirects(response, reverse('index'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_post_invalid(self):
        invalid_data = {
            'email': 'testuser@test.com',
            'password': 'wrongpassword',
        }
        response = self.client.post(self.url, invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')
        form = response.context['form']
        self.assertIsInstance(form, CustomAuthenticationForm)
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Неверный email или пароль')

    def test_post_invalid_empty_fields(self):
        empty_data = {
            'email': '',
            'password': '',
        }
        response = self.client.post(self.url, empty_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')
        form = response.context['form']
        self.assertIsInstance(form, CustomAuthenticationForm)
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Неверный email или пароль')