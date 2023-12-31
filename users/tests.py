from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth import get_user_model

from users.forms import CustomUserCreationForm, LoginForm
from users.models import CustomUser


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

    class AppLoginViewTestCase(TestCase):
        def setUp(self):
            self.client = Client()
            self.url = reverse('login')
            self.user_data = {
                'username': 'testuser',
                'password': 'testpassword',
            }
            self.user = CustomUser.objects.create_user(**self.user_data)

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
            self.assertContains(response,
                                'Please enter a correct username and password. Note that both fields may be case-sensitive.')

        def test_redirect_authenticated_user(self):
            self.client.login(**self.user_data)
            response = self.client.get(self.url)
            self.assertRedirects(response, reverse('index'))