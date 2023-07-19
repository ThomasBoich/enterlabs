from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from users.forms import CustomUserCreationForm


class RegisterModalViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('register_modal')
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@test.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        self.form_invalid_data = {
            'username': 'testuser',
            'email': 'testuser@test.com',
            'password1': 'testpassword',
            'password2': 'wrongpassword',
        }

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register_modal.html')
        form = response.context['form']
        self.assertIsInstance(form, CustomUserCreationForm)

    def test_post_valid(self):
        response = self.client.post(self.url, self.user_data)
        self.assertRedirects(response, reverse('index'))
        User = get_user_model()
        user = User.objects.get(username=self.user_data['username'])
        self.assertEqual(user.email, self.user_data['email'])

    def test_post_invalid(self):
        response = self.client.post(self.url, self.form_invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register_modal.html')
        form = response.context['form']
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(response, 'The two password fields didn&#x27;t match.')

    def test_password_recommendations(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register_modal.html')
        form = response.context['form']
        self.assertIsInstance(form, CustomUserCreationForm)
        recommendations = response.context['recommendations']
        self.assertEqual(recommendations, ['The password cannot be entirely numeric.', 'The password cannot be too similar to the username.', 'The password cannot be too common.', 'The password must contain at least 8 characters.'])