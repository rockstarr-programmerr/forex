# from shop.models import Product, Category

# top_phong_thuy = Product.objects.filter(available=True, top_phong_thuy=True)[:4]
# top_trang_tri = Product.objects.filter(available=True, top_trang_tri=True)[:4]
# top_suc_khoe = Product.objects.filter(available=True, top_suc_khoe=True)[:4]

# shop_categories = Category.objects.all()

# def footer_context(request):
# 	return {
# 		'top_phong_thuy': top_phong_thuy,
# 		'top_trang_tri': top_trang_tri,
# 		'top_suc_khoe': top_suc_khoe,
# 		'shop_categories': shop_categories,
# 	}