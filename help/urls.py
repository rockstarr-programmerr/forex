from django.urls import re_path
from . import views

app_name = 'help'

urlpatterns = [
	re_path(r'^$', views.help_list, name='help_list'),
	re_path(r'^chu-de/(?P<category_slug>[-\w\d]+)/$', views.help_list, name="help_list_by_category"),
	re_path(r'^(?P<slug>[-\w\d]+)/$', views.help_detail, name='help_detail'),
]