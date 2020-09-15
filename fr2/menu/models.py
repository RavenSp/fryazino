from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.html import format_html

# Create your models here.
class Menu(MPTTModel):

	title = models.CharField(max_length=150, unique=True, verbose_name='Пункт меню')
	url = models.CharField(max_length=100, verbose_name='URL', blank=True, null=True)
	active = models.BooleanField(verbose_name='Активная', default=True)
	parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',verbose_name='Родительский элемент')

	class MPTTMeta:
		order_insertion_by = ['title']

	class Meta:
		verbose_name='Пункт меню'
		verbose_name_plural='Главное меню'

	def __str__(self):

		return self.title

	def get_url(self):

		if hasattr(self, 'simplepage'):

			return self.simplepage.get_absolute_url()

		elif hasattr(self, 'category'):
			return self.category.get_absolute_url()

		elif hasattr(self, 'documents'):

			return self.documents.get_absolute_url()

		elif hasattr(self, 'news'):

			return self.news.get_absolute_url()

		elif self.url:

			return self.url
		else:
			return '#'

	def get_link(self):
		if self.get_url() == '#':
			return self.get_url()
		else:
			return format_html('<a href="%s" target="_blank">%s</a>' %(self.get_url(), self.get_url()))

	get_link.short_description = 'URL пункта меню'

class footerMenu(models.Model):


	title = models.CharField(max_length=255, verbose_name='Пункт меню')
	weight = models.IntegerField(verbose_name='Вес ссылки', help_text='Вес определяет положение ссылки в выводе меню. Более легкие ссылки будут наверху')
	slug = models.CharField(max_length=255, verbose_name='URL', blank=True, null=True)
	active = models.BooleanField(verbose_name='Активная', default=True)
	parrent = models.ForeignKey(Menu, verbose_name='Ссылка на пункт главного меню', blank=True, null=True, on_delete=models.SET_NULL)

	class Meta:

		verbose_name='Пункт нижнего меню'
		verbose_name_plural = 'Нижнее меню'

	def __str__(self):
		return self.title

	def get_url(self):
		if self.parrent:

			return self.parrent.get_url()

		elif self.slug:
			return self.slug

		else:
			return '#'

	def get_link(self):
		if self.get_url() == '#':
			return self.get_url()
		else:
			return format_html('<a href="%s" target="_blank">%s</a>' %(self.get_url(), self.get_url()))



class socialLinks(models.Model):

	title = models.CharField(max_length=50, verbose_name='Название соцсети')
	link = models.CharField(max_length=256, verbose_name='URL')
	linkClass = models.CharField(max_length=50, verbose_name='Класс значка fontawesome', help_text='Классы можно искать на сайте <a href="https://fontawesome.ru/all-icons/" target="_blank">https://fontawesome.ru/all-icons/</a>')
	color = models.CharField(max_length=7, verbose_name='Цвет знача при наведении', default='#0057c1')
	weight = models.IntegerField(verbose_name='Вес ссылки',
								 help_text='Вес определяет положение ссылки в выводе меню. Более легкие ссылки будут наверху')
	active = models.BooleanField(verbose_name='Активная', default=True)

	class Meta:

		verbose_name_plural = 'Значки соцсетей'
		verbose_name = 'Значок соцсети'

	def __str__(self):
		return self.title

	def get_icon(self):
		return format_html('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"><i class="fa %s" aria-hidden="true" style="font-size: 25px;" onmouseover="this.style.color=\'%s\';" onmouseout="this.style.color=\'black\';"></i>' % (self.linkClass, self.color))

	def get_link(self):
		return format_html('<a href="%s" target="_blank">%s</a>' % (self.link, self.link))



	get_icon.short_description = 'Пример иконки'
	get_link.short_description = 'URL'
