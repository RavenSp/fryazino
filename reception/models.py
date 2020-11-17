from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.mail import send_mail, EmailMultiAlternatives
from django.utils import dateformat
from datetime import datetime
# Create your models here.



class theme(models.Model):

	title = models.CharField(max_length= 200, verbose_name='Название темы')
	email = models.EmailField(verbose_name='E-mail рассылки', blank=True, null=True)

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

	theme = models.ForeignKey(theme, on_delete=models.PROTECT, verbose_name='Тема обращения', default='1')
	recipient = models.ForeignKey(recipient, on_delete=models.PROTECT, verbose_name='Адресат обращения')

	created = models.DateTimeField(verbose_name='Дата и время добавления обращения', auto_now_add=True)
	ipaddres = models.GenericIPAddressField(verbose_name='IP адрес')

	

	def addzero(self, zero=6):

		n = zero - len(str(self.id))

		if n > 0:

			return '0'*n + str(self.id)

		return str(self.id)

	class Meta:

		verbose_name = 'Обращение гражданина'
		verbose_name_plural = 'Обращения граждан'

		ordering = ['-created']



	def __str__(self):

			return 'Обращение №%s' % self.addzero()

	def send_email_after(self):

		mail_list = []

		mail_list.append(self.recipient.email)
		if self.theme.email:
			mail_list.append(self.theme.email)
		subject = 'Обращение в приёмную %s №%s по теме %s' % (self.recipient.title, self.addzero() ,self.theme.title)

		autor = '%s %s' % (self.first_name, self.last_name)

		if self.middle_name:
			autor +=  ' %s' % self.middle_name  
		if self.phone:
			phone = self.phone
		else:
			phone = 'Номер телефона не указан'

		message = '''
		ТЕКСТ ОБРАЩЕНИЯ:
		%s

		Номер обращения: %s
		Дата и время обращения: %s
		Тема обращения: %s
		Автор: %s
		Email: %s
		Телефон: %s
		''' % (self.message, self.addzero(), dateformat.format(datetime.now(), 'd E Y H:i'), self.theme.title, autor, self.email, phone)
		from_email = ''

		msg = EmailMultiAlternatives(subject, message, 'fryazino.vds@yandex.ru', mail_list)

		if self.file:

			msg.attach_file(self.file.path)

		msg.send()

	def sendback(self):

		autor = self.last_name
		if self.middle_name:
			autor += ' %s' % self.middle_name

		subject = 'Ваше обращение принято!'
		message = '''
		Уважаемый(ая) %s,
		Ваше обращение принято в работу!

		Текст обращения:
		%s

		Номер обращения: %s
		Дата обращения: %s

		Спасибо Вам за неравнодушную позицию и участие в общественной жизни городского округа Фрязино!
		''' % (autor, self.message, self.addzero(), dateformat.format(datetime.now(), 'd E Y'))

		
		msg = EmailMultiAlternatives(subject, message, 'fryazino.vds@yandex.ru', [self.email])

		if self.file:

			msg.attach_file(self.file.path)

		msg.send()