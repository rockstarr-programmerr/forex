from django.urls import path

from . import views

app_name = 'download'

urlpatterns = [
	path('', views.download_list, name='download_list'),
	path('<int:pk>/', views.download_detail, name='download_detail'),
]
