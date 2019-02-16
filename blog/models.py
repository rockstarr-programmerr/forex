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
	return 'blog_images/{new_filename}/{final_filename}'.format(new_filename=new_filename, final_filename=final_filename)

# Model managers and custom querysets:
class MyBlogPostQuerySet(models.QuerySet):
	def filter_by_search_blogs(self, request):
		if request.GET:
			query = request.GET.get('q')
			parameter = models.Q(name__icontains=query) | models.Q(hashtag__icontains=query) | models.Q(author__icontains=query) | models.Q(content__icontains=query) | models.Q(category__name__icontains=query) | models.Q(category__description__icontains=query)
			blogs = self.filter(parameter).distinct()
		return blogs 

class BlogPostManager(models.Manager):
	def get_queryset(self):
		return MyBlogPostQuerySet(self.model, using=self._db)
	def filter_by_search_blogs(self, request):
		return self.get_queryset().filter_by_search_blogs(request)

# Models
class BlogCategory(models.Model):
	name = models.CharField(max_length=255, db_index=True, verbose_name="Tên")
	slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", blank=True)
	description = models.TextField(blank=True, verbose_name="Mô tả")
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Tạo mới")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Cập nhật")

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-created_at']
		verbose_name = 'Danh mục blog'
		verbose_name_plural = 'Danh mục blog'

	def save(self):
		if not self.slug:
			self.slug = slugify(self.name.replace('đ', 'd'))
		super(BlogCategory, self).save()

	def get_absolute_url(self):
		return reverse('blog:blog_list_by_category', args=[self.slug])


class BlogPost(models.Model):
	category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, verbose_name="Danh mục")
	name = models.CharField(max_length=255, db_index=True, verbose_name="Tiêu đề")
	slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name="URL", blank=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Tạo mới")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Cập nhật")
	author = models.CharField(max_length=100, blank=True, verbose_name="Tác giả")
	hashtag = models.CharField(max_length=500, blank=True)
	main_img = models.ImageField(upload_to=upload_image_path, blank=True, verbose_name="Ảnh blog")

	content = RichTextUploadingField(blank=True, verbose_name="Nội dung")

	# paragraph_1 = models.TextField(blank=True, verbose_name="Đoạn 1")
	# img_1 = models.ImageField(upload_to=upload_image_path, blank=True, verbose_name="Ảnh 1")
	# img_description_1 = models.CharField(max_length=300, blank=True, verbose_name="Caption ảnh 1")
	# paragraph_2 = models.TextField(blank=True, verbose_name="Đoạn 2")
	# img_2 = models.ImageField(upload_to=upload_image_path, blank=True, verbose_name="Ảnh 2")
	# img_description_2 = models.CharField(max_length=300, blank=True, verbose_name="Caption ảnh 2")
	# paragraph_3 = models.TextField(blank=True, verbose_name="Đoạn 3")
	# img_3 = models.ImageField(upload_to=upload_image_path, blank=True, verbose_name="Ảnh 3")
	# img_description_3 = models.CharField(max_length=300, blank=True, verbose_name="Caption ảnh 3")
	# paragraph_4 = models.TextField(blank=True, verbose_name="Đoạn 4")
	# img_4 = models.ImageField(upload_to=upload_image_path, blank=True, verbose_name="Ảnh 4")
	# img_description_4 = models.CharField(max_length=300, blank=True, verbose_name="Caption ảnh 4")
	# paragraph_5 = models.TextField(blank=True, verbose_name="Đoạn 5")
	# img_5 = models.ImageField(upload_to=upload_image_path, blank=True, verbose_name="Ảnh 5")
	# img_description_5 = models.CharField(max_length=300, blank=True, verbose_name="Caption ảnh 5")
	# paragraph_6 = models.TextField(blank=True, verbose_name="Đoạn 6")
	# img_6 = models.ImageField(upload_to=upload_image_path, blank=True, verbose_name="Ảnh 6")
	# img_description_6 = models.CharField(max_length=300, blank=True, verbose_name="Caption ảnh 6")
	# paragraph_7 = models.TextField(blank=True, verbose_name="Đoạn 7")
	# img_7 = models.ImageField(upload_to=upload_image_path, blank=True, verbose_name="Ảnh 7")
	# img_description_7 = models.CharField(max_length=300, blank=True, verbose_name="Caption ảnh 7")
	# paragraph_8 = models.TextField(blank=True, verbose_name="Đoạn 8")
	# img_8 = models.ImageField(upload_to=upload_image_path, blank=True, verbose_name="Ảnh 8")
	# img_description_8 = models.CharField(max_length=300, blank=True, verbose_name="Caption ảnh 8")

	objects = BlogPostManager()

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-created_at']
		verbose_name = "Bài blog"
		verbose_name_plural = "Bài blog"

	def split_to_single_tags(self):
		single_tags = self.hashtag.split(', ')
		return single_tags

	def save(self):
		if not self.slug:
			self.slug = slugify(self.name.replace('đ', 'd'))
		super(BlogPost, self).save()

	def get_absolute_url(self):
		return reverse('blog:blog_detail', args=[self.slug])

class BlogComment(models.Model):
	blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, verbose_name="Bài blog")
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