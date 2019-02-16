from django.contrib import admin
from .models import Category, Product 

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'stt', 'slug']
	list_editable = ['stt']

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'stt', 'price', 'available', 'stock', 'created_at', 'updated_at']
	list_filter = ['available', 'created_at', 'updated_at', 'top_phong_thuy', 'top_trang_tri', 'top_suc_khoe']
	list_editable = ['price', 'stt', 'available', 'stock']

admin.site.register(Product, ProductAdmin)
