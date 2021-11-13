from django.urls import path
from .views import *
from .models import Product

urlpatterns = [
    path('', marketplace, name='marketplace-home'),   
    path('<int:product_id>/', product, name='marketplace-product'),     
]
