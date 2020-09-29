from django import template
from menu.models import Menu, footerMenu

register = template.Library()

@register.inclusion_tag('main-menu.html')
def main_menu():

	mMenu = Menu.objects.filter(active=True)

	return {'menu': mMenu}



@register.inclusion_tag('mobile-menu.html')
def mobile_menu():

	mMenu = Menu.objects.filter(active=True)

	return {'menu': mMenu}

@register.inclusion_tag('footer-menu.html')
def footer_menu():

	menu = footerMenu.objects.filter(active=True).order_by('weight')

	return {'menu': menu}