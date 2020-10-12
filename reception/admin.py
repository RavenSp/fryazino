from django.contrib import admin
from .models import theme, recipient, apperal

# Register your models here.


@admin.register(theme)
class ThemeAdmin(admin.ModelAdmin):

	pass

@admin.register(recipient)
class RecipientAdmin(admin.ModelAdmin):

	prepopulated_fields = {"slug": ("title",)}

@admin.register(apperal)
class ApperalAdmin(admin.ModelAdmin):

	list_display = ('__str__', 'created',)