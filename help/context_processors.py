from .models import HelpCategory

help_categories = HelpCategory.objects.all()

def nav_help_context(request):
	return {
		'help_categories': help_categories
	}
