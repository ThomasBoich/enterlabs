from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Category, Cart
from .serializers import CategorySerializer, CartSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Переопределяем метод get_queryset, чтобы получить только корзины, связанные с текущим пользователем.
        """
        user = self.request.user
        return Cart.objects.filter(user=user)


from .models import CartItem
from .serializers import CartItemSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Переопределяем метод get_queryset, чтобы получить только элементы корзины, связанные с корзиной текущего пользователя.
        """
        user = self.request.user
        return CartItem.objects.filter(cart__user=user)


from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Переопределяем метод get_queryset, чтобы получить только заказы, связанные с текущим пользователем.
        """
        user = self.request.user
        return Order.objects.filter(user=user)


from .models import OrderItem
from .serializers import OrderItemSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Переопределяем метод get_queryset, чтобы получить только элементы заказа, связанные с заказом текущего пользователя.
        """
        user = self.request.user
        return OrderItem.objects.filter(order__user=user)


from .models import Payment
from .serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Переопределяем метод get_queryset, чтобы получить только платежи, связанные с заказами текущего пользователя.
        """
        user = self.request.user
        return Payment.objects.filter(order__user=user)