from django.shortcuts import render, get_object_or_404
from products.models import Product

def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    return render(request, 'products/product_detail.html', {'product': product})

def home(request):
    # You can add any context or logic for your home page here
    return render(request, 'home.html')