from django.urls import path

from blog.views import blog, post
from shop.views import category, shop, item, cart
from subscribe.views import SubscribeView
from users.views import AppLogoutView, login_modal, register_modal
from .views import index, about, profile

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('blog/post/<int:post_id>/', post, name='post'),
    path('logout/', AppLogoutView.as_view(), name='logout'),
    path('register/', register_modal, name='register_modal'),
    path('login/', login_modal, name='login_modal'),
    path('shop/', shop, name='shop'),
    path('profile/', profile, name='profile'),
    path('subscribe/', SubscribeView.as_view(), name='subscribe_form'),
    path('shop/category/<int:cat_id>/', category, name='category'),
    path('shop/item/<int:item_id>/', item, name='item'),
    path('cart/', cart, name='cart'),
]