from django.shortcuts import render
from . import models
# Create your views here.

def return_home_page(request):
    return render(request, "accounts/main.html")

def return_products_page(request):
    return render(request, "accounts/products.html")

def return_customers_page(request):
    customers = models.Customer.objects.all()
    context = {"customers": customers}
    return render(request, "accounts/customers.html", context)