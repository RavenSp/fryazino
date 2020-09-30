from django.db import models
from django.utils.html import escape, format_html
from os import path

# Create your models here.



class Galery(models.Model):

	title = models.CharField(max_length=50, verbose_name='Наименование галери')
	slug = models.SlugField(max_length=50, verbose_name='URL', unique=True)
	description = models.TextField(verbose_name='Описание галери')
	active = models.BooleanField(verbose_name='Актвиная галерея', default=True)

	created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
	modifed = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)

	def __str__(self):

		return self.title

	class Meta:

		verbose_name='Галерея'
		verbose_name_plural = 'Галереи'
		ordering = ['created',]

	def get_absolute_url(self):

		return "galery/%s" % self.slug

	def get_images(self):

		if self.active:
			images = Image.objects.filter(galery=self.pk)

			return images

	def get_first_img(self):

		if self.active:
			images = Image.objects.filter(galery=self.pk)

			return images[0]

	def get_count(self):

		if self.active:
			images = Image.objects.filter(galery=self.pk)

			return len(images)



class Image(models.Model):

	title = models.CharField(verbose_name='Название изображения', max_length=50)
	image = models.ImageField(verbose_name='Изображение', upload_to='uploads/%Y/%m/%d/galery')
	galery = models.ForeignKey(Galery, on_delete=models.CASCADE, verbose_name='Галерея')


	class Meta:

		verbose_name='Изображение'
		verbose_name_plural = 'Изображения'
		ordering = ['id',]

	def __str__(self):

		return self.title





