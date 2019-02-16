from django.forms import ModelForm, TextInput, EmailInput, Textarea
from .models import Order

class OrderCreateForm(ModelForm):
	class Meta:
		model = Order 
		fields = ['full_name', 'phone_number', 'email', 'address', 'note']
		widgets = {
			'full_name': TextInput(attrs={'placeholder': 'Họ và tên *'}),
			'phone_number': TextInput(attrs={'placeholder': 'Số điện thoại *'}),
			'email': EmailInput(attrs={'placeholder': 'Email'}),
			'address': TextInput(attrs={'placeholder': 'Địa chỉ *'}),
			'note': Textarea(attrs={'placeholder': 'Chú thích'}),
		}