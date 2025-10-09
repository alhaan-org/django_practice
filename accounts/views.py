from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import *
from .forms import OrderForm, CreateUser
from .decorators import unauthorized_user, if_is_admin
# Create your views here.

@login_required(login_url="login")
def return_home_page(request):
    return render(request, "accounts/main.html")

@login_required(login_url="login")
def return_products_page(request):
    query = request.GET.get('query',None)
    if query:
        products = Product.objects.filter(title__icontains=query)
    else:
        products = Product.objects.all()
    
    product_context = {"products": products}
    return render(request, "accounts/products.html", product_context)

@login_required(login_url="login")
@if_is_admin(admin=True)
def return_customers_page(request):
    customer = Customer.objects.all()
    context = {"customer": customer}
    return render(request, "accounts/customers.html", context)

@login_required(login_url="login")
@if_is_admin(admin=True)
def return_customer_orders_page(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/customers")
    context = {"form" : form}
    return render(request, "accounts/customer_form.html", context)

@login_required(login_url="login")
@if_is_admin(admin=True)
def return_update_customers_page(request):
    return render(request, "accounts/update_customer.html")

@unauthorized_user
def return_login_page(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("products")
        else:
            messages.info(request, "Authentication Failed, Wrong Password and Email")
    
    context = {}
    return render(request, "accounts/login.html", context)


def return_logout(request):
    logout(request)
    return redirect("login")

@unauthorized_user
def return_signup_page(request):
    form = CreateUser()
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            user = form.save()

            group = Group.objects.get(name="customer")
            user.groups.add(group)
            Customer(
                user=user,
            )
            messages.success(request, f"Account was created successfully")
            return redirect("login")
            
    context = {"form" : form}
    return render(request, "accounts/signup.html", context)