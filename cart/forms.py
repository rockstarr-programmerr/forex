from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

class CartAddProductForm(forms.Form):
	quantity = forms.IntegerField(label='Số lượng', initial=1, min_value=1)
	update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)