from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from .cart import Cart
from products.models import Product

def cart_detail(request):
    return render(request, 'cart/detail.html')

def cart_add(request, product_id):

    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')
