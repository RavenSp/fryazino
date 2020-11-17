from django.contrib import admin
from .forms import DocsForm
from django.db import models
from .models import Page, TextBlock
from dal_admin_filters import AutocompleteFilter
from dal import autocomplete

# Register your models here.
'''
class DocsInline(admin.StackedInline):
	model = Page.docs.through
	extra = 1

	formfield_overrides = {
		models.ForeignKey: {'widget': autocomplete.ModelSelect2Multiple(url='/doc-autocomplete/')},
	}

'''



@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
	form = DocsForm
	prepopulated_fields = {"slug": ("title",)}
	list_display = ['title', 'publisdDate', 'publish']
	fields = (('title', 'slug'), ('keywords', 'seo_description'), ('publisdDate', 'publish'), 'body', 'galery', 'docs', 'menu')
	#inlines = [DocsInline]

	class Media:
		css = {'all' : ('https://cdn.jsdelivr.net/npm/select2@4.1.0-beta.1/dist/css/select2.min.css',),}
		js = ('https://cdn.jsdelivr.net/npm/select2@4.1.0-beta.1/dist/js/select2.min.js',)

	

@admin.register(TextBlock)
class TextblockAdmin(admin.ModelAdmin):
	list_display = ['title', 'key']
	