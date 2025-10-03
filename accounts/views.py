from django.shortcuts import render
from .models import *
# Create your views here.

def return_home_page(request):
    return render(request, "accounts/main.html")

def return_products_page(request):
    return render(request, "accounts/products.html")

def return_customers_page(request, pk):
    customer = Customer.objects.get(id=pk)
    context = {"customer": customer}
    return render(request, "accounts/customers.html", context)