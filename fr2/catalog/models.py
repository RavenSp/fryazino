from django.db import models
from menu.models import Menu
# Create your models here.

class TypeMUP(models.Model):

	title = models.CharField(max_length=50, verbose_name='Название')
	slug = models.SlugField(max_length=50, verbose_name='URL', unique=True)

	menu = models.OneToOneField(Menu, on_delete=models.SET_NULL, verbose_name='Пункт меню', blank=True, null=True)

	class Meta:

		verbose_name = 'Тип муниципального учреждения'
		verbose_name_plural = 'Типы муниципальных учреждений'

	def __str__(self):

		return self.title

	def get_absolute_url(self):

		return "/catalog/%s-%s/" % (self.id, self.slug)


class ListMUP(models.Model):

	type_mup = models.ForeignKey(TypeMUP, on_delete=models.CASCADE, verbose_name='Тип МУПа')
	title = models.CharField(max_length=150, verbose_name='Официальное полное название', unique=True)
	shortTitle = models.CharField(max_length=40, verbose_name='Сокращенное назвение', unique=True)
	boss = models.CharField(max_length=512, verbose_name='ФИО руководителя')
	bossPhone = models.CharField(max_length=20, verbose_name='Телефон руководителя', help_text='Если телефонов несколько, введите их через запятую')
	zam = models.CharField(max_length=512, verbose_name='ФИО заместителя руководителя', blank=True, null=True)
	zamPhone = models.CharField(max_length=20, verbose_name='Телефон заместителя', help_text='Если телефонов несколько, введите их через запятую', blank=True, null=True)
	description = models.TextField(verbose_name='Описание целей и задач учреждения', blank=True, null=True)
	postAddress = models.TextField(verbose_name='Почтовый адрес учреждения')
	email = models.CharField(max_length=256, verbose_name='E-mail учреждения', blank=True, null=True)
	fax = models.CharField(max_length=150, verbose_name='Факс учреждения', blank=True, null=True)
	phone = models.CharField(max_length=256, verbose_name='Телефон учреждения', help_text='Если телефонов несколько, введите их через запятую')

	def __str__(self):

		return self.shortTitle

	def get_absolute_url(self):

		return "/catalog/%s-%s/" % (self.type_mup, self.slug)

	class Meta:

		verbose_name = 'Муниципальное учреждение'
		verbose_name_plural = 'Муниципальные учреждения'
