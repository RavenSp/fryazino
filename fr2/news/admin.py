from django.contrib import admin
from .models import News, Category
from image_cropping import ImageCroppingMixin
from django.utils.translation import gettext_lazy as _
# Register your models here.

@admin.register(News)
class NewsAdmin(ImageCroppingMixin, admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	#fields =  (('title', 'slug'), ('keywords', 'seo_description'), ('image_tag', 'image_in_body'), 'min_free_cropping', 'topNews', ('category', 'tags'), ('publish', 'publisdDate'), 'news_text', 'menu' )
	readonly_fields = ('image_tag',)
	list_display = ('title', 'publisdDate', 'category', 'publish', 'topNews')
	date_hierarchy = 'publisdDate'
	list_filter = ('publisdDate', 'tags', 'category', 'topNews')
	ordering = ['-publisdDate']
	search_fields = ['title']

	fieldsets = (
		(None, {
			'fields': (('title', 'slug',), ('keywords', 'seo_description',),'image', ('image_in_body', 'topNews'))}),
		(_('Обрезка изображения'), {
			'classes':('grp-collapse grp-closed',),
			'fields': (('min_free_cropping','list_img_cropping','top_news_cropping'),)
			}),
		(None, {
			'fields':(('category', 'tags'), ('publish', 'publisdDate'), 'news_text')
			}),
		(_('Дополнительные опции'), {
			'classes':('grp-collapse grp-closed',),
			'fields': ('menu',)
			})

			 )
		

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	list_display = ['title', 'get_link']
	ordering = ['pk']
