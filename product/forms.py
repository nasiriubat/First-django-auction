from django import forms

from .models import Product


class CreateProductForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = ['title', 'details', 'image','minBidPrice','end_date']
