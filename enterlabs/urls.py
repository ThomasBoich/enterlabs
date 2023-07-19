"""
URL configuration for enterlabs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from blog.views import PostViewSet
from shop.views import CategoryViewSet, CartViewSet, CartItemViewSet, OrderViewSet, PaymentViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="API documentation",
    ),
    public=True,
)
router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'carts', CartViewSet)
router.register(r'cart-items', CartItemViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include(router.urls)),
    path('api/', include(router.urls)),
    path('api/', include(router.urls)),
    path('api/', include(router.urls)),
    path('api/', include(router.urls)),
    path('api/', include(router.urls)),
    path('api/', include(router.urls)),
    # path('blog/', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = settings.ADMIN_SITE_HEADER