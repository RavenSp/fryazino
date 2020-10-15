from django.contrib import admin
from .models import theme, recipient, apperal

# Register your models here.


@admin.register(theme)
class ThemeAdmin(admin.ModelAdmin):

	list_display = ('title', 'email')

@admin.register(recipient)
class RecipientAdmin(admin.ModelAdmin):
	list_display = ('title', 'email')
	prepopulated_fields = {"slug": ("title",)}

@admin.register(apperal)
class ApperalAdmin(admin.ModelAdmin):

	list_display = ('__str__', 'recipient','created', 'ipaddres',)
	date_hierarchy = 'created'
	list_filter = ('recipient',  'theme', 'created')