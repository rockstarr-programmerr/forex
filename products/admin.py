from django.contrib import admin

from .models import ForexProduct

class ForexProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'stt', 'image']
	list_editable = ['stt']

admin.site.register(ForexProduct, ForexProductAdmin)
