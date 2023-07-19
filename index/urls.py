from django.urls import path

from blog.views import blog, post
from users.views import AppLogoutView, login_modal, register_modal
from .views import index, about, shop

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('blog/post/<int:post_id>/', post, name='post'),
    path('logout/', AppLogoutView.as_view(), name='logout'),
    path('register/', register_modal, name='register_modal'),
    path('login/', login_modal, name='login_modal'),
    path('shop/', shop, name='shop'),
]