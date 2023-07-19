from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from users.forms import CustomUserCreationForm, CustomAuthenticationForm


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


# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(request, email=email, password=password)
#             login(request, user)
#             return redirect('index')
#     else:
#         form = CustomUserCreationForm()
#     return render(request, {'form': form})

def shop(request):
    context = {
        'title': 'Магазин витаминов',
    }
    return render(request, 'index/shop.html', context)