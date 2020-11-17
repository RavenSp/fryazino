from django.contrib import admin
from image_cropping import ImageCroppingMixin
from .models import bigBanner, mBanner

# Register your models here.

@admin.register(bigBanner)
class BigbannerAdmin(admin.ModelAdmin):
	list_display = ['title', 'url', 'active']
	readonly_fields = ('image_tag',)
	fields = ['title', 'url', 'active', 'image', 'image_tag']

@admin.register(mBanner)
class MbannerAdmin(ImageCroppingMixin, admin.ModelAdmin):
	list_display = ['title', 'url', 'active']