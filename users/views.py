from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from users.forms import LoginForm, CustomUserCreationForm


# Create your views here.

class AppLoginView(LoginView):
    form_class = LoginForm
    template_name = 'header.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        return reverse_lazy('index')

    redirect_authenticated_user = True


class AppLogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('index')

def login_modal(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'index.html', {'form': form})


def register_modal(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    recommendations = form.get_password_recommendations()
    return render(request, 'register_modal.html', {'form': form, 'recommendations': recommendations})