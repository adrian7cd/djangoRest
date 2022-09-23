from django import forms 

from .models import Product, Products

class ProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = [
      "title",
      "content",
      "price"
    ]