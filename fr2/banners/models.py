from django.db import models
from taggit.managers import TaggableManager
from image_cropping import ImageRatioField, ImageCropField
from django.utils.html import escape, format_html

# Create your models here.


class bigBanner(models.Model):

	title = models.CharField(verbose_name='Название', max_length=50)
	url = models.CharField(verbose_name='URL', max_length=50, blank=True, null=True)
	active = models.BooleanField(verbose_name='Активный', default=True)
	tags = TaggableManager(verbose_name='Темы')
	image = models.ImageField(upload_to='uploads/big-banners/', verbose_name='Изображение')


	class Meta:

		verbose_name='Большой баннер'
		verbose_name_plural = 'Большие баннеры'

	def __str__(self):

		return self.title

	def image_tag(self):

		return format_html('<img src="%s" width="600px" />' % escape(self.image.url))

	image_tag.short_description = 'Изображение'
	image_tag.allow_tags = True

class mBanner(models.Model):

	title = models.CharField(verbose_name='Название', max_length=50)
	url = models.CharField(verbose_name='URL', max_length=50, blank=True, null=True)
	active = models.BooleanField(verbose_name='Активный', default=True)
	tags = TaggableManager(verbose_name='Темы')
	image = models.ImageField(upload_to='uploads/m-banners/', verbose_name='Изображение')
	cropping = ImageRatioField('image', '280x176', verbose_name='Обрезка баннера')


	class Meta:

		verbose_name='Баннер'
		verbose_name_plural = 'Баннеры для карусели'

	def __str__(self):

		return self.title

	def get_url(self):

		if self.url:
			return self.url

		else:
			return '#'