from django.forms import ModelForm, Form

from .models import apperal

class ApperalForm(ModelForm):

	class Meta:

		model = apperal

		fields = ['first_name', 'last_name', 'middle_name', 'post_address', 'email', 'phone', 'theme', 'message', 'file', 'personal']
