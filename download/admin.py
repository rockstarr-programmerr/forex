from django.contrib import admin

from .models import DownloadItem, DownloadSymbol

class DownloadSymbolInline(admin.StackedInline):
	model = DownloadSymbol
	extra = 0

class DownloadItemAdmin(admin.ModelAdmin):
	list_display = ['name', 'stt', 'available']
	list_editable = ['stt', 'available']
	inlines = [DownloadSymbolInline]

admin.site.register(DownloadItem, DownloadItemAdmin)
