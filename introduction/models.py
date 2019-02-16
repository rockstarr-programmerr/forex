import random
import os

from django.db import models
from colorfield.fields import ColorField
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
	return 'banner_images/{new_filename}/{final_filename}'.format(new_filename=new_filename, final_filename=final_filename)


# Create your models here.

class Introduction(models.Model):
	name = models.CharField(max_length=50, unique=True, verbose_name='Tên')
	content = RichTextUploadingField(blank=True, verbose_name="Nội dung")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-updated_at']

	def __str__(self):
		return self.name 

class Banner(models.Model):
	img = models.ImageField(upload_to=upload_image_path, verbose_name="Ảnh")
	text_1 = models.CharField(max_length=500, blank=True)
	color_1 = ColorField(default='#ffffff', blank=True)
	text_2 = models.CharField(max_length=500, blank=True)
	color_2 = ColorField(default='#ffffff', blank=True)
	text_3 = models.CharField(max_length=500, blank=True)
	color_3 = ColorField(default='#ffffff', blank=True)
	text_4 = models.CharField(max_length=500, blank=True)
	color_4 = ColorField(default='#ffffff', blank=True)

	def __str__(self):
		return 'Banner #' + str(self.pk)