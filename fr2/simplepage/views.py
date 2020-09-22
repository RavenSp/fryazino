from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView

from .models import Page

# Create your views here.


class PageView(DetailView):

	model = Page

	def get(self, request, pg):

		page = get_object_or_404(Page, slug=pg, publish=True)

		return render(request, 'page.html', {'page':page})