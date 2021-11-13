from django.shortcuts import render
from .models import Product

def marketplace(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request,'marketplace/shop.html',context)

def product(request):
    return render(request, 'marketplace/detail.html')