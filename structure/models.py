from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.html import format_html
from ckeditor_uploader.fields import RichTextUploadingField
from menu.models import Menu

# Create your models here.
class TypeElement(models.Model):

	title = models.CharField(max_length=200, verbose_name='Название')


class Structure(MPTTModel):

	title = models.CharField(max_length=200, verbose_name='Название')
	typeStruct = models.ForeignKey(TypeElement, on_delete=models.PROTECT, verbose_name='Тип элемента')
	func  = RichTextUploadingField(verbose_name='Полномочия, задачи, фукнции')
	


	active = models.BooleanField(verbose_name='Активный', default=True)
	parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',verbose_name='Родительский элемент')