from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.



class theme(models.Model):

	title = models.CharField(max_length= 200, verbose_name='Название темы')
	email = models.EmailField(verbose_name='E-mail рассылки')

	def __str__(self):

		return self.title

	class Meta:

		verbose_name='Тема обращения'
		verbose_name_plural = 'Темы обращения'
		ordering = ['id']


class recipient(models.Model):

	title = models.CharField(max_length=200, verbose_name='Получатель')
	email = models.EmailField(verbose_name='Email')
	slug = models.SlugField(max_length=50, verbose_name='URL')

	def __str__(self):

		return self.title

	class Meta:

		verbose_name = 'Получатель обращения'
		verbose_name_plural = 'Получатели обращений'

		ordering = ['id']




class apperal(models.Model):

	first_name = models.CharField(verbose_name='Фамилия', max_length=200)
	last_name = models.CharField(max_length=200, verbose_name='Имя')
	middle_name = models.CharField(max_length=200, verbose_name='Отчество', blank=True, null=True)
	post_address = models.CharField(verbose_name='Почтовый адрес',  max_length=500)
	email = models.EmailField(verbose_name='E-mail')
	phone = models.CharField(verbose_name='Телефон',max_length=12, blank=True, null=True)
	message = models.TextField(verbose_name='Сообщение')

	file = models.FileField(upload_to='reception/%Y/%m/%d/', verbose_name='Приложенный файл', blank=True)
	personal = models.BooleanField(verbose_name='Согласие на обработку персональных данных', default=False)

	theme = models.ForeignKey(theme, on_delete=models.PROTECT, verbose_name='Тема обращения')
	recipient = models.ForeignKey(recipient, on_delete=models.PROTECT, verbose_name='Адресат обращения')

	created = models.DateTimeField(verbose_name='Дата и время добавления обращения', auto_now_add=True)
	ipaddres = models.GenericIPAddressField(verbose_name='IP адрес')

	def __str__(self):

		return 'Обращение №%s' % (self.id)

	class Meta:

		verbose_name = 'Обращение гражданина'
		verbose_name_plural = 'Обращения граждан'

		ordering = ['-created']



