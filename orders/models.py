from django.db import models
from products.models import ForexProduct

# Create your models here.

class Order(models.Model):
	full_name = models.CharField('Họ và tên', max_length=100)
	phone_number = models.CharField('Số điện thoại', max_length=20)
	email = models.EmailField(blank=True)
	address = models.CharField('Địa chỉ', max_length=150)
	note = models.TextField('Chú thích', blank=True)
	created = models.DateTimeField('Thời gian', auto_now_add=True)
	updated = models.DateTimeField('Cập nhật', auto_now=True)
	delivered = models.BooleanField('Giao hàng', default=False)
	paid = models.BooleanField('Thanh toán', default=False)

	class Meta:
		ordering = ['-created']
		verbose_name = 'Đơn hàng'
		verbose_name_plural = 'Đơn hàng'

	def __str__(self):
		return 'Order #{}'.format(self.id)

	def get_total_cost(self):
		return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
	order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='Đơn hàng')
	product = models.ForeignKey(ForexProduct, related_name='order_items', on_delete=models.CASCADE, verbose_name='Sản phẩm')
	unit_price = models.DecimalField(max_digits=12, decimal_places=0, verbose_name='Đơn giá')
	quantity = models.IntegerField(default=0, verbose_name='Số lượng')
	total_price = models.DecimalField(max_digits=12, decimal_places=0, default=0, verbose_name='Thành tiền')

	def __str__(self):
		return '#{}'.format(self.id)

	def get_cost(self):
		return self.price * self.quantity 