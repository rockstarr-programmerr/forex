from django.urls import re_path
from . import views

app_name = 'search'

urlpatterns = [
	re_path(r'^$', views.search_view, name='search_view'),
	re_path(r'^hashtags/$', views.search_view_by_hashtags, name='search_view_by_hashtags'),
]