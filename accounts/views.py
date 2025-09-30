from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def return_home_page(request):
    return render(request, "accounts/main.html")

def return_products_page(request):
    return render(request, "accounts/products.html")

def return_customers_page(request):
    return render(request, "accounts/customers.html")