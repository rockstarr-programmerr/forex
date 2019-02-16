from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import HelpPost, HelpCategory, HelpComment
from .forms import HelpCommentForm

# Create your views here.

def help_list(request, category_slug=None):
	category = None
	categories = HelpCategory.objects.all()
	helps = HelpPost.objects.all()

	if category_slug:
		category = get_object_or_404(HelpCategory, slug=category_slug)
		helps = HelpPost.objects.filter(category=category)

	paginator = Paginator(helps, 15)
	current_page = request.GET.get('page')
	helps = paginator.get_page(current_page)
	try:
		int_current_page = int(current_page)
	except TypeError:
		int_current_page = 1

	context = {
		'helps': helps,
		'category': category,
		'categories': categories,
		'paginator': paginator,
		'int_current_page': int_current_page,
	}

	return render(request, 'help/help_list.html', context)

def help_detail(request, slug):
	help_post = get_object_or_404(HelpPost, slug=slug)
	related_post = HelpPost.objects.filter(category=help_post.category).exclude(slug=slug)[:5]
	comments = HelpComment.objects.filter(help_post=help_post, allow=True)

	try:
		prev_post = HelpPost.objects.filter(pk__lt=help_post.pk)[0]
	except IndexError:
		prev_post = None

	try:
		next_post = HelpPost.objects.filter(pk__gt=help_post.pk).order_by('pk')[0]
	except IndexError:
		next_post = None

	form = HelpCommentForm()
	if request.POST:
		form = HelpCommentForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			HelpComment.objects.create(
					author = cd['author'],
					email = cd['email'],
					content = cd['content'],
					help_post = help_post,
					allow = True,
				)
			return redirect('help:help_detail', slug=slug)

	context = {
		'help_post': help_post,
		'related_post': related_post,
		'prev_post': prev_post,
		'next_post': next_post,
		'form': form,
		'comments': comments,
	}

	return render(request, 'help/help_detail.html', context)