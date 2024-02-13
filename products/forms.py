from django import forms
from products.models import Product,Reviews

class CreateProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name','description','price','category','image']

# class ProductImageForm(forms.ModelForm):
#     class Meta:
#         model = ProductImage
#         fields = ['image']
#         attrs={'multiple': True}


class ProductEditForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['name','description','price','category','image']


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Reviews
        fields = ['text',]
