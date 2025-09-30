from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=255, null=False)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=255, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.title

class Customers(models.Model):
    STATUS = (
        ("Paid", "Paid"),
        ("Not Paid", "Not Paid"),
        ("Delivered", "Delivered")
    )

    name = models.CharField(max_length=255, null=False)
    phone_number = models.CharField(max_length=15, null=False)
    status = models.CharField(max_length=255, null=False, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.name

