from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Galery, Image
from django.views.generic import ListView, DetailView
# Create your views here.


class GaleryDetailView(DetailView):

	model = Galery

	def get(self, request, url):

		galery = get_object_or_404(Galery, slug=url)

		context = {'galery': galery}

		return render(request, 'galeryDetail.html', context)


class GaleryListView(ListView):

	model = Galery

	def get(self, request):

		galeryList = get_list_or_404(Galery, active=True)

		title = 'Фотоархив'

		context = {
			'title':title,
			'galery_list':galeryList
		}

		return render(request, 'galeryList.html', context)