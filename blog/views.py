from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import BlogPost, BlogCategory, BlogComment
from .forms import BlogCommentForm

# Create your views here.

def blog_list(request, category_slug=None):
	category = None
	categories = BlogCategory.objects.all()
	blogs = BlogPost.objects.all()

	if category_slug:
		category = get_object_or_404(BlogCategory, slug=category_slug)
		blogs = BlogPost.objects.filter(category=category)

	paginator = Paginator(blogs, 15)
	current_page = request.GET.get('page')
	blogs = paginator.get_page(current_page)
	try:
		int_current_page = int(current_page)
	except TypeError:
		int_current_page = 1

	context = {
		'blogs': blogs,
		'category': category,
		'categories': categories,
		'paginator': paginator,
		'int_current_page': int_current_page,
	}

	return render(request, 'blog/blog_list.html', context)

def blog_detail(request, slug):
	blog_post = get_object_or_404(BlogPost, slug=slug)
	related_post = BlogPost.objects.filter(category=blog_post.category).exclude(slug=slug)[:5]
	comments = BlogComment.objects.filter(blog_post=blog_post, allow=True)

	try:
		prev_post = BlogPost.objects.filter(pk__lt=blog_post.pk)[0]
	except IndexError:
		prev_post = None

	try:
		next_post = BlogPost.objects.filter(pk__gt=blog_post.pk).order_by('pk')[0]
	except IndexError:
		next_post = None

	form = BlogCommentForm()
	if request.POST:
		form = BlogCommentForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			BlogComment.objects.create(
					author = cd['author'],
					email = cd['email'],
					content = cd['content'],
					blog_post = blog_post,
					allow = True,
				)
			return redirect('blog:blog_detail', slug=slug)

	context = {
		'blog_post': blog_post,
		'related_post': related_post,
		'prev_post': prev_post,
		'next_post': next_post,
		'form': form,
		'comments': comments,
	}

	return render(request, 'blog/blog_detail.html', context)