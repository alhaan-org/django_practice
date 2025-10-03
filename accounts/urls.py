from django.urls import path
from . import views

urlpatterns = [
    path("", views.return_home_page, name='home'),
    path("products/", views.return_products_page, name="products"),
    path("customers/<str:pk>/", views.return_customers_page, name="customers")
]
