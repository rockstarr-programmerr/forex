from django.shortcuts import render

from products.models import ForexProduct
from introduction.models import Introduction, Banner

def index(request):
	free_products = ForexProduct.objects.filter(available=True, price=0)
	paid_products = ForexProduct.objects.filter(available=True, price__gt=0)

	try:
		introduction = Introduction.objects.get(name='Main introduction')
	except Introduction.DoesNotExist:
		introduction = Introduction.objects.create(name='Main introduction', content='')

	banners = Banner.objects.all()

	context = {
		'free_products': free_products,
		'paid_products': paid_products,
		'introduction': introduction,
		'banners': banners,
	}

	return render(request, 'base/index.html', context)
