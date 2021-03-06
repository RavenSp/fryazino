from django.db import models
#from taggit.managers import TaggableManager
from taggit_autosuggest.managers import TaggableManager
from taggit.models import TaggedItemBase

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from image_cropping import ImageRatioField, ImageCropField
from django.utils.html import escape, format_html
from mptt.models import MPTTModel, TreeOneToOneField
from django.db.models import Q

from menu.models import Menu
from photogalery.models import Galery

class TaggedNews(TaggedItemBase):
    content_object = models.ForeignKey('News', on_delete=models.CASCADE)

class Category(models.Model):

	title = models.CharField(max_length=250, verbose_name='Название категории')
	slug = models.SlugField(verbose_name='URL')
	menu = TreeOneToOneField(Menu, on_delete=models.SET_NULL, verbose_name='Пункт меню', blank=True, null=True)


	def __str__(self):

		return self.title

	def get_absolute_url(self):

		return "/news/category/%s/" % (self.slug)

	def get_link(self):
		if self.slug == '#':
			return self.get_url()
		else:
			return format_html('<a href="%s" target="_blank">%s</a>' %(self.get_absolute_url(), self.get_absolute_url()))

	get_link.short_description = 'URL'




	class Meta:

		verbose_name='Категория'
		verbose_name_plural='Категории'

class News(models.Model):

	title = models.CharField(max_length=250, verbose_name='Название')
	keywords = models.CharField(max_length=500, verbose_name='Ключевые слова', help_text='Введите ключевые слова для SEO через запятую!')
	seo_description = models.CharField(max_length=500, verbose_name='SEO описание', help_text='SEO описание новости. Не более 500 символов')
	slug = models.SlugField(verbose_name='URL')
	created = models.DateTimeField(auto_now_add=True)
	modifed = models.DateTimeField(auto_now=True)

	image = ImageCropField(upload_to='uploads/%Y/%m/%d/', verbose_name='Изображение новости', blank=True)
	min_free_cropping = ImageRatioField('image', '200x100', free_crop=True, verbose_name='Обрезка фото')

	list_img_cropping = ImageRatioField('image', '4x3')
	top_news_cropping = ImageRatioField('image', '16x9')

	image_in_body = models.BooleanField(verbose_name='Вставить изображение в материал', default=False)
	category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.PROTECT)
	topNews = models.BooleanField(verbose_name='В главные новости', default=False)
	tags = TaggableManager(verbose_name='Темы')
	news_text = RichTextUploadingField(verbose_name='Текст статьи')
	galery = models.ForeignKey(Galery, verbose_name='Галерея изображений', blank=True, null=True, on_delete=models.SET_NULL)
	menu = TreeOneToOneField(Menu, on_delete=models.SET_NULL, verbose_name='Пункт меню', blank=True, null=True)
	publisdDate = models.DateTimeField(verbose_name='Дата публикации', default=timezone.now)
	publish = models.BooleanField(verbose_name='Опубликовано', default=True)

	
	def __str__(self):

		return self.title

	def image_tag(self):

		return format_html('<img src="%s" width="200px" />' % escape(self.image.url))

	image_tag.short_description = 'Изображение'
	image_tag.allow_tags = True



	def get_absolute_url(self):

		return "/news/%s-%s/" % (self.id, self.slug)

	def search(que):

		if que:

			or_lookup = (Q(title__icontains=que) | Q(news_text__icontains=que))

			qs = News.objects.filter(or_lookup, publish=True, publisdDate__lte=timezone.now())

			return qs

		return None

	def pub_date(self):

		return self.publisdDate
		

	def searchType(self):

		return 'Новость'


	class Meta:

		verbose_name='Новость'
		verbose_name_plural='Новости'
