from django.contrib import admin
from .models import DocsAuthor, Documents
from image_cropping import ImageCroppingMixin
from django.utils.translation import gettext_lazy as _
# Register your models here.


@admin.register(DocsAuthor)
class DocsAuthorAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ["title",]}
	ordering = ['title']

@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	list_display = ['title', 'Author', 'docDate', 'publisdDate', 'publish']
	date_hierarchy = 'docDate'
	list_filter = ['docDate', 'publisdDate', 'Author']


admin.site.site_header = "Администрация городского округа Фрязино"

admin.site.site_title = 'Официальный сайт городского округа Фрязино'
