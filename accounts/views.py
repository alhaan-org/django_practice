from django.shortcuts import redirect, render
from .models import *
from .forms import OrderForm
# Create your views here.

def return_home_page(request):
    return render(request, "accounts/main.html")

def return_products_page(request):
    products = Product.objects.all()
    product_context = {"products": products}
    return render(request, "accounts/products.html", product_context)

def return_customers_page(request):
    customer = Customer.objects.all()
    context = {"customer": customer}
    return render(request, "accounts/customers.html", context)

def return_customer_orders_page(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/customers")
    context = {"form" : form}
    return render(request, "accounts/customer_form.html", context)


def return_update_customers_page(request):
    return render(request, )