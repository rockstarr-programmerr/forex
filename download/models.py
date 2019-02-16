from django.db import models
from django.urls import reverse


class DownloadItem(models.Model):
	name = models.CharField('Tên item', max_length=100)
	stt = models.IntegerField(blank=True, null=True)
	image = models.ImageField('Ảnh', upload_to='products_img/download_item', blank=True, null=True)
	available = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('download:download_detail', args=(self.pk,))

	class Meta:
		ordering = ['stt', '-updated_at']

class DownloadSymbol(models.Model):
	name = models.CharField('Symbol', max_length=100)
	download_item = models.ForeignKey(DownloadItem, on_delete=models.CASCADE)
	stt = models.IntegerField(blank=True, null=True)
	link_6_months = models.URLField('Link 6 tháng', max_length=500, blank=True, null=True)
	link_1_year = models.URLField('Link 1 năm', max_length=500, blank=True, null=True)
	link_2_years = models.URLField('Link 2 năm', max_length=500, blank=True, null=True)
	link_5_years = models.URLField('Link 5 năm', max_length=500, blank=True, null=True)
	available = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str(self):
		return self.name

	class Meta:
		ordering = ['stt', '-updated_at']
