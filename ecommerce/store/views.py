from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Order

def store_home(request):
    return render(request, 'store/home.html')

def category_overview(request):
    categories = Category.objects.all()
    return render(request, 'store/category_overview.html', {'categories': categories})

def category_page(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'store/category_page.html', {'category': category, 'products': products})

def product_page(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_page.html', {'product': product})

def cart(request):
    return render(request, 'store/cart.html')

def checkout(request):
    return render(request, 'store/checkout.html')

def account(request):
    return render(request, 'store/account.html')
