from .models import BlogCategory

blog_categories = BlogCategory.objects.all()

def nav_context(request):
	return {
		'blog_categories': blog_categories,
	}