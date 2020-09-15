from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView
from .models import News, Category
from taggit.models import Tag
from django.utils import timezone
# Create your views here.


class CategoryNewsListView(ListView):

	model = News

	def get(self, request, cat):

		category = get_object_or_404(Category, slug=cat)

		list = get_list_or_404(self.model.objects.filter(category__title=category, publish=True).order_by('-publisdDate'))

		tag_cloud = self.model.tags.most_common()[:10]


		context = {
			'news':list,
			'title': category.title,
			'tag_cloud':tag_cloud,
		}
		return render(request, 'list_view.html', context)

class NewsListView(ListView):

	model = News

	def get(self, request):

		list = self.model.objects.filter(publish=True, publisdDate__lt=timezone.now()).order_by('-publisdDate')

		tag_cloud = self.model.tags.most_common()[:10]

		context = {
			'news':list,
			'title': 'Последние новости',
			'tag_cloud':tag_cloud,
		}
		return render(request, 'list_view.html', context)


class TagNewsListView(ListView):

	model = News

	def get(self, request, tag_slug):

		tag = Tag.objects.get(slug=tag_slug)

		list = get_list_or_404(News.objects.filter(tags__slug__in=[tag_slug], publish=True, publisdDate__lt=timezone.now()).order_by('-publisdDate'))		

		tag_cloud = self.model.tags.most_common()[:10]


		context = {
			'news':list,
			'title': tag.name,
			'tag_cloud':tag_cloud,
		}
		return render(request, 'list_view.html', context)

class NewsDetailView(DetailView):

	model = News

	def get(self, request, id, slug):

		new = get_object_or_404(News, pk=id, slug=slug)

		print(new.title)

		tag_cloud = self.model.tags.most_common()[:12]

		context = {
			'new':new,
			'tag_cloud':tag_cloud,
		}

		return render(request, 'news_detail.html', context)