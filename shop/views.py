from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Category, Cart, Product
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



def shop(request):
    categories = Category.objects.all()
    items = Product.objects.all()
    context = {
        'title': 'Магазин витаминов',
        'categories': categories,
        'products': items,
    }
    return render(request, 'index/shop.html', context)


def category(request, cat_id):
    categories = Category.objects.all()
    products = Product.objects.filter(category=cat_id)
    category = Category.objects.get(id=cat_id)
    context = {
        'title': '',
        'categories': categories,
        'products': products,
        'category': category,
    }
    return render(request, 'index/category.html', context)

def item(request, item_id):
    categories = Category.objects.all()
    item = Product.objects.get(id=item_id)
    context = {
        'title': '',
        'categories': categories,
        'item': item,
    }
    return render(request, 'index/item.html', context)

@login_required
def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = cart.items.all()
    total_cost = cart.get_total_cost()
    return render(request, 'index/cart.html', {'cart_items': cart_items, 'total_cost': total_cost})

def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity', 1)
        product = get_object_or_404(Product, pk=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += int(quantity)
        cart_item.save()
        referer = request.META.get('HTTP_REFERER')
        if referer:
            # Если есть заголовок Referer, выполняем редирект на эту страницу
            return HttpResponseRedirect(referer)
        else:
            # Иначе возвращаем ответ в формате JSON
            return JsonResponse({'success': True})
    return JsonResponse({'success': False})