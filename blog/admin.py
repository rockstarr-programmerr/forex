from django.contrib import admin
from .models import BlogCategory, BlogPost, BlogComment

# Register your models here.

class BlogCategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'created_at', 'updated_at']

admin.site.register(BlogCategory, BlogCategoryAdmin)

class BlogPostAdmin(admin.ModelAdmin):
	list_display = ['name', 'author', 'created_at']

admin.site.register(BlogPost, BlogPostAdmin)

class BlogCommentAdmin(admin.ModelAdmin):
	list_display = ['author', 'content', 'created_at', 'email', 'allow']
	list_editable = ['allow']

admin.site.register(BlogComment, BlogCommentAdmin)