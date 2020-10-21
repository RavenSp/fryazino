from django.contrib import admin
from .models import TypeMUP, ListMUP

# Register your models here.

@admin.register(TypeMUP)
class TypeMupAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	

@admin.register(ListMUP)
class ListMupAdmin(admin.ModelAdmin):
	pass