from rest_framework import serializers
from .models import Category, Cart, CartItem, Order, OrderItem, Payment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id', 'user', 'created', 'updated')


class CartItemSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()

    class Meta:
        model = CartItem
        fields = ('id', 'cart', 'product', 'quantity')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'user', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'created', 'updated', 'paid')

class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()

    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'product', 'price', 'quantity')

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'order', 'payment_method', 'payment_date', 'amount')