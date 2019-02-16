from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Category, Product
from introduction.models import Introduction, Banner
from cart.forms import CartAddProductForm

from products.models import ForexProduct

# Create your views here.

def index_page(request):
	# products = Product.objects.filter(available=True)[:20]

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
	return render(request, 'shop/index.html', context)

def product_list(request, category_slug=None, price_range=None, usage_0=None, usage_1=None, usage_2=None, usage_3=None, usage_4=None, usage_5=None, usage_6=None,):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)

	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = Product.objects.filter(category=category, available=True)

	if request.GET:
		products = Product.objects.filter(available=True).filter_by_price(request).filter_by_usage(request)
		price_range = request.GET.get('gia') # For checked in templates
		usage_0 = request.GET.get('usage_0')
		usage_1 = request.GET.get('usage_1')
		usage_2 = request.GET.get('usage_2')
		usage_3 = request.GET.get('usage_3')
		usage_4 = request.GET.get('usage_4')
		usage_5 = request.GET.get('usage_5')
		usage_6 = request.GET.get('usage_6')

	if category_slug and request.GET:
		category = get_object_or_404(Category, slug=category_slug)
		products = Product.objects.filter(category=category, available=True).filter_by_price(request).filter_by_usage(request)

	# Show 30 products per page:
	paginator = Paginator(products, 30)
	current_page = request.GET.get('page')
	products = paginator.get_page(current_page)

	# For showing what is the current page in template:
	try:
		int_current_page = int(current_page)
	except TypeError:
		int_current_page = 1

	context = {
		'category': category,
		'categories': categories,
		'products': products,
		'paginator': paginator,
		'int_current_page': int_current_page,
		'category_slug': category_slug,
		'price_range': price_range,
		'usage_0': usage_0,
		'usage_1': usage_1,
		'usage_2': usage_2,
		'usage_3': usage_3,
		'usage_4': usage_4,
		'usage_5': usage_5,
		'usage_6': usage_6,
	}

	return render(request, 'shop/product/list.html', context)

def product_detail(request, id, slug):
	product = get_object_or_404(Product, id=id, slug=slug, available=True)
	products_of_same_category = Product.objects.filter(category=product.category, available=True).exclude(id=id)
	cart_product_form = CartAddProductForm()

	# Show 20 related products per page:
	paginator = Paginator(products_of_same_category, 20)
	current_page = request.GET.get('page')
	products_of_same_category = paginator.get_page(current_page)

	# For showing what is the current page in template:
	try:
		int_current_page = int(current_page)
	except TypeError:
		int_current_page = 1

	context = {
		'product': product,
		'products_of_same_category': products_of_same_category,
		'cart_product_form': cart_product_form,
		'paginator': paginator,
		'int_current_page': int_current_page,
	}
	return render(request, 'shop/product/detail.html', context)
