from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin, MPTTModelAdmin
from .models import Menu, footerMenu, socialLinks, allSitesMenu
# Register your models here.

@admin.register(Menu)
class MenuMPTTAdmin(DraggableMPTTAdmin):
	list_display = ['tree_actions','indented_title', 'get_link', 'active']
	list_display_links = ['indented_title']

@admin.register(footerMenu)
class FootermenuAdmin(admin.ModelAdmin):
	list_display = ['title', 'weight', 'get_link', 'active']
	list_display_links = ['title',]
	list_editable = ['weight']
	ordering = ['weight', 'title']

@admin.register(socialLinks)
class SociallinksAdmin(admin.ModelAdmin):
	list_display = ['title', 'weight','color', 'get_link', 'get_icon', 'active']
	list_display_links = ['title', ]
	list_editable = ['weight']
	ordering = ['weight', 'title']

@admin.register(allSitesMenu)
class AllSitesMenuAdmin(admin.ModelAdmin):

	list_display = ['title', 'typeSite', 'url', 'active']
	ordering = ['id']