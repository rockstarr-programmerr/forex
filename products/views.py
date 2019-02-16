from django.shortcuts import render, get_object_or_404

from .models import ForexProduct


def product_list(request):
	products = ForexProduct.objects.filter(available=True)

	context = {
		'products': products
	}

	return render(request, 'products/product_list.html', context)

# def product_detail(request, pk):
# 	product = get_object_or_404(ForexProduct, pk=pk)

# 	context = {
# 		'product': product
# 	}

# 	return render(request, 'products/product_detail.html', context)
