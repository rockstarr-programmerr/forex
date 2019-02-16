from django.contrib import admin
from .models import Introduction, Banner

# Register your models here.

class IntroductionAdmin(admin.ModelAdmin):
	list_display = ['name', 'created_at', 'updated_at']

admin.site.register(Introduction, IntroductionAdmin)

admin.site.register(Banner)