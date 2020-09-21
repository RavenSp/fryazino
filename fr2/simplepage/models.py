from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from menu.models import Menu
from django.utils import timezone
from mptt.models import MPTTModel, TreeOneToOneField
# Create your models here.


class Page(models.Model):

	title = models.CharField(max_length=700, verbose_name='Заголовок')
	keywords = models.CharField(max_length=500, verbose_name='Ключевые слова', help_text='Введите ключевые слова для SEO через запятую!')
	seo_description = models.CharField(max_length=500, verbose_name='SEO описание', help_text='SEO описание новости. Не более 500 символов')
	slug = models.SlugField(verbose_name='URL', unique=True)
	created = models.DateTimeField(auto_now_add=True)
	modifed = models.DateTimeField(auto_now=True)

	body = RichTextUploadingField(verbose_name='Текст страницы')

	menu = TreeOneToOneField(Menu, on_delete=models.SET_NULL, verbose_name='Пункт меню', blank=True, null=True)
	publisdDate = models.DateTimeField(verbose_name='Дата публикации', default=timezone.now)
	publish = models.BooleanField(verbose_name='Опубликовано', default=True)

	class Meta:

		verbose_name='Страница'
		verbose_name_plural = 'Страницы'

	def __str__(self):

		return self.title

	def get_absolute_url(self):

		return self.slug

class TextBlock(models.Model):

	title = models.CharField(max_length=50, verbose_name='Название')
	title_in_block = models.BooleanField(verbose_name='Отображать название блока', default=False)
	key = models.CharField(max_length=50, verbose_name='Ключ блока', unique=True, help_text='Ключ только на английском языке')
	blockclass = models.CharField(max_length=50, verbose_name='Класс div текстовго блока', blank=True, null=True)
	body = RichTextUploadingField(verbose_name='Текст блока')

	class Meta:

		verbose_name = 'Текстовый блок'
		verbose_name_plural = 'Тестовые блоки'

	def __str__(self):

		return self.title
