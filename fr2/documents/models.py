from django.db import models
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from image_cropping import ImageRatioField, ImageCropField
from django.utils.html import escape, format_html


from menu.models import Menu

# Create your models here.


class DocsAuthor(models.Model):

	title = models.CharField(max_length=250, verbose_name='Наименование органа')
	slug = models.SlugField(verbose_name='URL')

	def __str__(self):

		return self.title

	def get_absolute_url(self):

		return "/docauth/%s-%s/" % (self.id, self.slug)

	class Meta:

		verbose_name='Орган принявший документ'
		verbose_name_plural='Органы принимающие документы'





class Documents(models.Model):

	title = models.CharField(max_length=700, verbose_name='Название')
	slug = models.SlugField(verbose_name='URL')
	
	number = models.CharField(max_length=20, verbose_name='Номер документа', blank=True, null=True)
	Author = models.ForeignKey(DocsAuthor, on_delete=models.SET_NULL, verbose_name='Орган, принявший документ', blank=True, null=True)
	docDate = models.DateField(verbose_name='Дата подписания документа', default=timezone.now)
	descrpition = models.TextField(verbose_name='Описание документа', blank=True, null=True)

	publisdDate = models.DateTimeField(verbose_name='Дата публикации', default=timezone.now)
	publish = models.BooleanField(verbose_name='Опубликовано', default=True)
	file = models.FileField(upload_to='uploads/%Y/%m/%d/documents', verbose_name='Документ')

	def __str__(self):

		return self.title

	def get_absolute_url(self):

		return "/documents/%s/" % self.slug

	class Meta:

		verbose_name='Документ'
		verbose_name_plural='Документы'