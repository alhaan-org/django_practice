from django.forms import ModelForm
from .models import Customer

class OrderForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"