from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from shop.models import Category, Product
from blog.models import BlogPost

# Create your views here.

def search_view(request):
	'''
	Search for both Products(name, description, category) and Blog posts (name, content)
	'''
	# Products =====================
	products = Product.objects.filter(available=True).filter_by_search_products(request)
	# Blog posts =====================
	posts = BlogPost.objects.filter_by_search_blogs(request)
	# Showing query in templates:
	view_query = request.GET.get('q')
	# Show 30 searched products per page:
	paginator = Paginator(products, 30)
	current_page = request.GET.get('page')
	products = paginator.get_page(current_page)
	# For showing what is the current page in template:
	try:
		int_current_page = int(current_page)
	except TypeError:
		int_current_page = 1

	context = {
		'products': products,
		'posts': posts,
		'view_query': view_query,
		'paginator': paginator,
		'int_current_page': int_current_page,
	}

	return render(request, 'search/search_page.html', context)

def search_view_by_hashtags(request):
	posts = BlogPost.objects.filter_by_search_blogs(request)
	view_query = request.GET.get('q')
	context = {
		'posts': posts,
		'view_query': view_query,
	}

	return render(request, 'search/search_page.html', context)