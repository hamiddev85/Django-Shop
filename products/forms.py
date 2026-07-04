from django import forms
from .models import Product, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'category',
            'name',
            'slug',
            'price',
            'stock',
            'image',
            'description',
            'is_available',
        ]


    widgets = {
        'description': forms.Textarea(attrs={'rows': 4}),
    }