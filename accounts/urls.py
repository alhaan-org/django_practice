from django.urls import path
from . import views

urlpatterns = [
    path("", views.return_home_page,name='home'),
    path("products/", views.return_products_page),
    path("customers/", views.return_customers_page)
]
