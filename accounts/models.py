from django.db import models

# Create your models here.
class Tag(models.Model):

    title = models.CharField(max_length=50, null=False)
    zip_code = models.CharField(max_length=6, null=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=255, null=False)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=255, null=True)
    product_url = models.CharField(max_length=255, null=True)
    tags = models.ManyToManyField(Tag)
    date_created = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.title

class Customer(models.Model):
    STATUS = (
        ("Paid", "Paid"),
        ("Not Paid", "Not Paid"),
        ("Delivered", "Delivered")
    )

    name = models.CharField(max_length=255, null=False)
    phone_number = models.CharField(max_length=15, null=False)
    status = models.CharField(max_length=255, null=False, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=False)
    products = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
