from django.contrib import admin

from .models import ForexProduct

class ForexProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'stt', 'image', 'available']
	list_editable = ['stt', 'image', 'available']

admin.site.register(ForexProduct, ForexProductAdmin)
