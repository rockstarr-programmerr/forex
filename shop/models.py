import random
import os

from django.db import models
from django.urls import reverse
from django.db.models import Q
from django.template.defaultfilters import slugify


# Fancy stuffs first=============================================================================

def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext 

def upload_image_path(instance, filename):
	new_filename = 'trung-awesome-programmer-{random_integer}'.format(random_integer=random.randint(1, 145146)) 
	name, ext = get_filename_ext(filename)
	final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
	return 'products/{new_filename}/{final_filename}'.format(new_filename=new_filename, final_filename=final_filename)


# Custom querysets and model manager because I'm smart: -================================================================

class MyProductQuerySet(models.QuerySet):
	def filter_by_usage(self, request):
		if request.GET:
			usage_0 = request.GET.get('usage_0')
			usage_1 = request.GET.get('usage_1')
			usage_2 = request.GET.get('usage_2')
			usage_3 = request.GET.get('usage_3')
			usage_4 = request.GET.get('usage_4')
			usage_5 = request.GET.get('usage_5')
			usage_6 = request.GET.get('usage_6')

			products = self.all()

			if usage_1 == 'trang-tri':
				products = products.filter(cd_trang_tri=True) 
			if usage_2 == 'loc-khong-khi':
				products = products.filter(cd_loc_khong_khi=True) 
			if usage_3 == 'chua-benh':
				products = products.filter(cd_chua_benh=True) 
			if usage_4 == 'gia-vi':
				products = products.filter(cd_gia_vi=True) 
			if usage_5 == 'phong-thuy':
				products = products.filter(cd_phong_thuy=True) 
			if usage_6 == 'nha-o2':
				products = products.filter(cd_nha_o2=True)
			if usage_0 == 'tat-ca':
				products = self.all()

		return products

	def filter_by_price(self, request):
		if request.GET:
			price_range = request.GET.get('gia')

			products = self.all()

			if price_range == '50-200':
				products = products.filter(price__gte=50000, price__lte=200000)
			if price_range == '200-1000':
				products = products.filter(price__gte=200000, price__lte=1000000)
			if price_range == '1000':
				products = products.filter(price__gte=1000000)

		return products 

	def filter_by_search_products(self, request):
		if request.GET:
			query = request.GET.get('q')
			parameter = Q(name__icontains=query) | Q(description__icontains=query) | Q(category__name__icontains=query)
			products = self.filter(parameter).distinct()

		return products


class ProductManager(models.Manager):
	def get_queryset(self):
		return MyProductQuerySet(self.model, using=self._db)

	def filter_by_usage(self, request):
		return self.get_queryset().filter_by_usage(request)
	
	def filter_by_price(self, request):
		return self.get_queryset().filter_by_price(request)

	def filter_by_search_products(self, request):
		return self.get_queryset().filter_by_search_products(request)



# Models below =============================================================================================================

class Category(models.Model):
	name = models.CharField(max_length=50, db_index=True, verbose_name='Tên danh mục')
	slug = models.SlugField(max_length=50, db_index=True, unique=True, verbose_name="URL", blank=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Tạo mới")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Cập nhật")
	stt = models.PositiveIntegerField(default=100)

	class Meta:
		ordering = ['stt']
		verbose_name = 'Danh mục'
		verbose_name_plural = 'Danh mục'

	def __str__(self):
		return self.name 

	def save(self):
		if not self.slug:
			self.slug = slugify(self.name.replace('đ', 'd'))
		super(Category, self).save()

	def get_absolute_url(self):
		return reverse('shop:product_list_by_category', args=[self.slug])


class Product(models.Model):
	category = models.ForeignKey(Category, related_name='products', on_delete=models.PROTECT, verbose_name="Danh mục")
	name = models.CharField(max_length=100, db_index=True, verbose_name="Tên cây")
	stt = models.PositiveIntegerField(default=1000, verbose_name="STT")
	slug = models.SlugField(max_length=100, db_index=True, verbose_name="URL", blank=True)
	description = models.TextField(blank=True, verbose_name="Mô tả")
	price = models.DecimalField(max_digits=12, decimal_places=0, verbose_name="Giá")
	available = models.BooleanField(default=True)
	stock = models.PositiveIntegerField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True, verbose_name="Tạo mới")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Cập nhật")
	image = models.ImageField(upload_to=upload_image_path, blank=True, verbose_name="Ảnh")
	cd_trang_tri = models.BooleanField(verbose_name='Công dụng: Trang trí', default=False)
	cd_loc_khong_khi = models.BooleanField(verbose_name='Công dụng: Lọc không khí', default=False)
	cd_chua_benh = models.BooleanField(verbose_name='Công dụng: Chữa bệnh', default=False)
	cd_gia_vi = models.BooleanField(verbose_name='Công dụng: Gia vị', default=False)
	cd_phong_thuy = models.BooleanField(verbose_name='Công dụng: Phong thủy', default=False)
	cd_nha_o2 = models.BooleanField(verbose_name='Công dụng: Nhả O2 ban đêm', default=False)
	top_phong_thuy = models.BooleanField(verbose_name='Top cây phong thủy', default=False)
	top_trang_tri = models.BooleanField(verbose_name='Top cây trang trí', default=False)
	top_suc_khoe = models.BooleanField(verbose_name='Top cây tốt cho sức khỏe', default=False)

	objects = ProductManager()

	class Meta:
		ordering = ['stt', '-created_at']
		verbose_name = 'Sản phẩm'
		verbose_name_plural = 'Sản phẩm'
		index_together = [['id', 'slug'],]

	def save(self):
		if not self.slug:
			self.slug = slugify(self.name.replace('đ', 'd'))
		super(Product, self).save()

	def __str__(self):
		return self.name 

	def get_absolute_url(self):
		return reverse('shop:product_detail', args=[self.id, self.slug])