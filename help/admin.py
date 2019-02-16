from django.contrib import admin
from .models import HelpCategory, HelpPost, HelpComment

# Register your models here.

class HelpCategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'created_at', 'updated_at']

admin.site.register(HelpCategory, HelpCategoryAdmin)

class HelpPostAdmin(admin.ModelAdmin):
	list_display = ['name', 'author', 'created_at']

admin.site.register(HelpPost, HelpPostAdmin)

class HelpCommentAdmin(admin.ModelAdmin):
	list_display = ['author', 'content', 'created_at', 'email', 'allow']
	list_editable = ['allow']

admin.site.register(HelpComment, HelpCommentAdmin)