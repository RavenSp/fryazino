from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import Http404
from django.views.generic import ListView, DetailView
from dal import autocomplete
from .models import Page
from documents.models import Documents

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

					menu = list(page.menu.get_children().filter(active=True))

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

class DocumentsAutocompile(autocomplete.Select2QuerySetView):

	def get_queryset(self):
		# Don't forget to filter out results depending on the visitor !
		if not self.request.user.is_superuser:
			raise Http404()

		qs = Documents.objects.filter(publish=True)

		if self.q:

			qs = qs.filter(title__icontains=self.q)

		return qs