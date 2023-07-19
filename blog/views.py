from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from blog.models import Post
from users.forms import CustomUserCreationForm


# Create your views here.

def blog(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, email=email, password=password)
            login(request, user)
            return redirect('blog')
    else:
        form = CustomUserCreationForm()
        template = 'blog/index.html'
        context = {
            'posts': Post.objects.all(),
            'form': form,
            'title': 'Блог',
        }
    return render(request, template, context)

def post(request, post_id):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, email=email, password=password)
            login(request, user)
            return redirect('post')
    else:
        form = CustomUserCreationForm()

        template = 'blog/post.html'
        context = {
            'post': Post.objects.get(id=post_id),
            'form': form,
            'title':f'{Post.objects.get(id=post_id).title}',
        }
    return render(request, template, context)



from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]