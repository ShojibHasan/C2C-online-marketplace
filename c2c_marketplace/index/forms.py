from django import forms

from product.models import Product


class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kargs):
        super(ProductForm, self).__init__(*args, **kargs)

    class Meta:
         model = Product
         fields = '__all__'
