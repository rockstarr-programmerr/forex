from django.shortcuts import render
from cart.cart import Cart 
from .models import OrderItem
from .forms import OrderCreateForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def order_create(request):
	cart = Cart(request)
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			order = form.save()
			for item in cart:
				if item['quantity'] > 0:
					OrderItem.objects.create(
						order = order,
						product = item['product'],
						unit_price = item['price'],
						quantity = item['quantity'],
						total_price = item['price'] * item['quantity'],
						)
			cart.clear()

			cd = form.cleaned_data
			email_subject = 'Đơn hàng mới'
			from_email = settings.EMAIL_HOST_USER
			to_email = [from_email]
			email_message = "Đơn hàng mới: Tên: %s; Điện thoại: %s; Email: %s; Địa chỉ: %s; Chú thích: %s"%(
				cd['full_name'],
				cd['phone_number'],
				cd['email'],
				cd['address'],
				cd['note']
				)

			send_mail(
			    email_subject,
			    email_message,
			    from_email,
			    to_email,
			    fail_silently=True,
			)

		return render (request, 'orders/order/created.html', {'order': order})
	else:
		form = OrderCreateForm()
		return render (request, 'orders/order/create.html', {'form': form})
