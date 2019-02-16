from django.db import models
from django.template.defaultfilters import slugify

from ckeditor_uploader.fields import RichTextUploadingField


class ForexProduct(models.Model):
	name = models.CharField('Thời hạn', max_length=255)
	stt = models.IntegerField(blank=True, null=True)
	image = models.ImageField(upload_to='forex_products', blank=True, null=True)
	note = RichTextUploadingField('Ghi chú', blank=True, null=True)
	price = models.IntegerField('Giá')
	available = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['stt', '-updated_at']
		verbose_name = 'Sản phẩm'
		verbose_name_plural = 'Sản phẩm'

	def __str__(self):
		return self.name

	# def get_absolute_url(self):
	# 	return reverse('products:product_detail', args=(self.pk,))
