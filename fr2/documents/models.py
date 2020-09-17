from django.db import models
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from image_cropping import ImageRatioField, ImageCropField
from django.utils.html import escape, format_html
import os

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


class DocType(models.Model):

	title = models.CharField(max_length=200, verbose_name='Тип документа')
	slug = models.SlugField(max_length=200, unique=True, verbose_name='URL')

	def get_absolute_url(self):

		return "doctype/%s/" % self.slug

	class Meta:

		verbose_name = 'Тип документов'
		verbose_name_plural = 'Типы документов'

	def __str__(self):

		return self.title





class Documents(models.Model):

	title = models.CharField(max_length=700, verbose_name='Название')
	slug = models.SlugField(max_length=200, verbose_name='URL', unique=True)
	
	number = models.CharField(max_length=20, verbose_name='Номер документа', blank=True, null=True)
	Author = models.ForeignKey(DocsAuthor, on_delete=models.SET_NULL, verbose_name='Орган, принявший документ', blank=True, null=True)
	TypeDoc = models.ForeignKey(DocType, on_delete=models.SET_NULL, verbose_name='Тип документа', blank = True, null=True)
	docDate = models.DateField(verbose_name='Дата подписания документа', default=timezone.now)
	descrpition = models.TextField(verbose_name='Описание документа', blank=True, null=True)

	publishDate = models.DateTimeField(verbose_name='Дата публикации', default=timezone.now)
	publish = models.BooleanField(verbose_name='Опубликовано', default=True)
	file = models.FileField(upload_to='uploads/%Y/%m/%d/documents', verbose_name='Документ')

	def __str__(self):

		return self.title

	def get_absolute_url(self):

		return "/documents/%s/" % self.slug

	def get_slug(self):
		return "%s-%s" % (self.pk, self.title) 

	def extension(self):
		extension = os.path.splitext(self.file.name)[-1][1:]
		return extension

	class Meta:

		verbose_name='Документ'
		verbose_name_plural='Документы'

	def save(self):
		super(Documents, self).save()
		if not self.slug.endswith('-' + str(self.id)):
			self.slug += '-' + str(self.id)
			super(Documents, self).save()