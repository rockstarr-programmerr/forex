from django.shortcuts import render

from products.models import ForexProduct
from introduction.models import Introduction, Banner

def index(request):
	forex_products = ForexProduct.objects.filter(available=True)

	try:
		introduction = Introduction.objects.get(name='Main introduction')
	except Introduction.DoesNotExist:
		introduction = Introduction.objects.create(name='Main introduction', content='')

	banners = Banner.objects.all()

	context = {
		'products': forex_products,
		'introduction': introduction,
		'banners': banners,
	}

	return render(request, 'base/index.html', context)
