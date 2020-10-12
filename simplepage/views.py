from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView

from .models import Page

# Create your views here.


class PageView(DetailView):

	model = Page

	def get(self, request, pg):

		page = get_object_or_404(Page, slug=pg, publish=True)

		context = {
			'page':page,
			
			}

		if page.menu:

			if page.menu.level <= 1:

				if page.menu.get_children():

					menu = list(page.menu.get_children())

					menu.insert(0, page.menu)

					context['submenu'] = menu
				else:

					menu = []
					context['submenu'] = menu

			else:

				menu = list(page.menu.parent.get_children()) 

				menu.insert(0, page.menu.parent)

				context['submenu'] = menu

		

		




		return render(request, 'page.html', context)