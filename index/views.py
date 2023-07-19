from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from users.forms import CustomUserCreationForm, CustomAuthenticationForm, UserUpdateForm


# Create your views here.


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Неверный email или пароль')
        else:
            messages.error(request, 'Неверный email или пароль')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def index(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, email=email, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
        context = {
            'title': 'Главная страница',
            'form': form,
        }
    return render(request, 'index/index.html', context )

def about(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, email=email, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
        context = {
            'title': 'О Компании',
            'form': form,
        }
    return render(request, 'index/about.html', context)


def shop(request):
    context = {
        'title': 'Магазин витаминов',
    }
    return render(request, 'index/shop.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form = form.save(commit=False)
            form.phone = '+' + ''.join([char for char in form.phone if char.isdigit()])
            form.save()
            messages.success(request, f'Ваш профиль успешно обновлен.')
            return redirect('profile')

    else:
       form = UserUpdateForm(instance=request.user)

    return render(request, 'index/profile.html', {'form': form,})