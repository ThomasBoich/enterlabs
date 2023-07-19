from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User

from users.forms import LoginForm


class AppLoginViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('login')
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword',
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_form_valid(self):
        response = self.client.post(self.url, self.user_data)
        self.assertRedirects(response, reverse('index'))

    def test_form_invalid(self):
        invalid_data = {
            'username': 'testuser',
            'password': 'wrongpassword',
        }
        response = self.client.post(self.url, invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'header.html')
        form = response.context['form']
        self.assertIsInstance(form, LoginForm)
        self.assertContains(response, 'Please enter a correct username and password. Note that both fields may be case-sensitive.')

    def test_redirect_authenticated_user(self):
        self.client.login(**self.user_data)
        response = self.client.get(self.url)
        self.assertRedirects(response, reverse('index'))