from django.forms import ModelForm, Form, ValidationError
from captcha.fields import CaptchaField

from .models import apperal

class ApperalForm(ModelForm):
	captcha = CaptchaField(label='Введите символы с картинки')

	class Meta:

		model = apperal

		fields = ['first_name', 'last_name', 'middle_name', 'post_address', 'email', 'phone', 'theme', 'message', 'file', 'personal']

	def clean_personal(self):

		personal = self.cleaned_data.get('personal')

		if not personal:

			raise ValidationError('Согласие на обработку персональных данных обязательно!')

		return personal

	