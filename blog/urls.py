from django.urls import re_path
from . import views

app_name = 'blog'

urlpatterns = [
	re_path(r'^$', views.blog_list, name='blog_list'),
	re_path(r'^chu-de/(?P<category_slug>[-\w\d]+)/$', views.blog_list, name="blog_list_by_category"),
	re_path(r'^(?P<slug>[-\w\d]+)/$', views.blog_detail, name='blog_detail'),
]