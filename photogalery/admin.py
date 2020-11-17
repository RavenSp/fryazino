from django.contrib import admin
from .models import Galery, Image

# Register your models here.

class ImageInline(admin.TabularInline):

	model = Image

@admin.register(Galery)
class GaleryAdmin(admin.ModelAdmin):

	prepopulated_fields = {'slug':('title',)}
	inlines = [ImageInline]

