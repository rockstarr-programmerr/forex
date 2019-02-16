import random
import os

from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField

# Fancy stuffs first=============================================================================

def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext 

def upload_image_path(instance, filename):
	new_filename = 'trung-awesome-programmer-{random_integer}'.format(random_integer=random.randint(1, 145146)) 
	name, ext = get_filename_ext(filename)
	final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
	return 'help_images/{new_filename}/{final_filename}'.format(new_filename=new_filename, final_filename=final_filename)

# Model managers and custom querysets:
class MyHelpPostQuerySet(models.QuerySet):
	def filter_by_search_helps(self, request):
		if request.GET:
			query = request.GET.get('q')
			parameter = models.Q(name__icontains=query) | models.Q(hashtag__icontains=query) | models.Q(author__icontains=query) | models.Q(content__icontains=query) | models.Q(category__name__icontains=query) | models.Q(category__description__icontains=query)
			helps = self.filter(parameter).distinct()
		return helps 

class HelpPostManager(models.Manager):
	def get_queryset(self):
		return MyHelpPostQuerySet(self.model, using=self._db)
	def filter_by_search_helps(self, request):
		return self.get_queryset().filter_by_search_helps(request)

# Models
class HelpCategory(models.Model):
	name = models.CharField(max_length=255, db_index=True, verbose_name="Tên")
	slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", blank=True)
	description = models.TextField(blank=True, verbose_name="Mô tả")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Tạo mới")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Cập nhật")

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-created_at']
		verbose_name = 'Danh mục help'
		verbose_name_plural = 'Danh mục help'

	def save(self):
		if not self.slug:
			self.slug = slugify(self.name.replace('đ', 'd'))
		super(HelpCategory, self).save()

	def get_absolute_url(self):
		return reverse('help:help_list_by_category', args=[self.slug])


class HelpPost(models.Model):
	category = models.ForeignKey(HelpCategory, on_delete=models.CASCADE, verbose_name="Danh mục")
	name = models.CharField(max_length=255, db_index=True, verbose_name="Tiêu đề")
	slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name="URL", blank=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Tạo mới")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Cập nhật")
	author = models.CharField(max_length=100, blank=True, verbose_name="Tác giả")
	hashtag = models.CharField(max_length=500, blank=True)
	main_img = models.ImageField(upload_to=upload_image_path, blank=True, verbose_name="Ảnh help")

	content = RichTextUploadingField(blank=True, verbose_name="Nội dung")

	objects = HelpPostManager()

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-created_at']
		verbose_name = "Bài help"
		verbose_name_plural = "Bài help"

	def split_to_single_tags(self):
		single_tags = self.hashtag.split(', ')
		return single_tags

	def save(self):
		if not self.slug:
			self.slug = slugify(self.name.replace('đ', 'd'))
		super(HelpPost, self).save()

	def get_absolute_url(self):
		return reverse('help:help_detail', args=[self.slug])

class HelpComment(models.Model):
	help_post = models.ForeignKey(HelpPost, on_delete=models.CASCADE, verbose_name="Bài help")
	author = models.CharField(max_length=100, verbose_name="Tác giả")
	email = models.EmailField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Tạo mới")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Cập nhật")
	content = models.TextField(verbose_name="Nội dung", max_length=2000)
	allow = models.BooleanField(default=True, blank=True, verbose_name="Cho phép")

	def __str__(self):
		return self.author

	class Meta:
		ordering = ['-updated_at']
		verbose_name = "Bình luận"
		verbose_name_plural = "Bình luận"