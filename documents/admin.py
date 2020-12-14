from django.contrib import admin
from .models import DocsAuthor, Documents, DocType, DocCategory, AddDocs
from image_cropping import ImageCroppingMixin
from mptt.admin import DraggableMPTTAdmin, MPTTModelAdmin
from django.utils.translation import gettext_lazy as _
from dal_admin_filters import AutocompleteFilter
# Register your models here.

class AddDocsInline(admin.TabularInline):

	model = AddDocs
	extra = 2



@admin.register(DocsAuthor)
class DocsAuthorAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ["title",]}
	ordering = ['title']

@admin.register(DocType)
class DocTypeAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ["title"]}
	ordering = ['title']

@admin.register(DocCategory)
class DocCategoryMPTTAdmin(DraggableMPTTAdmin):
	prepopulated_fields = {"slug": ["title"]}

@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	list_display = ['title', 'Author', 'docDate', 'publishDate', 'publish']
	date_hierarchy = 'docDate'
	list_filter = ['docDate', 'publishDate', 'Author', 'DocCategory']

	inlines = [
		AddDocsInline,
	]


admin.site.site_header = "Администрация городского округа Фрязино"

admin.site.site_title = 'Официальный сайт городского округа Фрязино'
