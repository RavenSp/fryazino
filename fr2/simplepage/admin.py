from django.contrib import admin
from .models import Page, TextBlock

# Register your models here.


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
	list_display = ['title', 'publisdDate', 'publish']
	fields = (('title', 'slug'), ('keywords', 'seo_description'), ('publisdDate', 'publish'), 'body', 'menu')


@admin.register(TextBlock)
class TextblockAdmin(admin.ModelAdmin):
	list_display = ['title', 'key']
	