from django.urls import re_path
from . import views

app_name = 'shop'

urlpatterns = [
	re_path(r'^$', views.index_page, name='index_page'),
	re_path(r'^san-pham/$', views.product_list, name='product_list'),
	re_path(r'^san-pham/(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
	re_path(r'^san-pham/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]