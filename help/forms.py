from django.forms import ModelForm, TextInput, EmailInput, Textarea

from .models import HelpComment

class HelpCommentForm(ModelForm):
	class Meta:
		model = HelpComment
		fields = ['author', 'email', 'content']
		widgets = {
			'author': TextInput(attrs={
					'placeholder': 'Tên *',
					'class': 'my-1 maven_font form-control',
					'style': 'font-size: 15px;',
				}),
			'email': EmailInput(attrs={
					'placeholder': 'Email',
					'class': 'my-1 maven_font form-control',
					'style': 'font-size: 15px;',
				}),
			'content': Textarea(attrs={
					'placeholder': 'Nội dung *',
					'class': 'my-1 maven_font form-control',
					'style': 'height: 110px; font-size: 15px;',
				}),
		}