from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView
from .models import News, Category
from taggit.models import Tag
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from sovet.models import deputat
# Create your views here.


NUMBER_PAGE = 10



class CategoryNewsListView(ListView):

	model = News
	

	def get(self, request, cat):

		category = get_object_or_404(Category, slug=cat)

		listNews = get_list_or_404(self.model.objects.filter(category__title=category, publish=True).order_by('-publisdDate'))

		page = request.GET.get('page', 1)

		paginator = Paginator(listNews, NUMBER_PAGE)

		try:
			listNews = paginator.page(page)
		except PageNotAnInteger:
			listNews = paginator.page(1)
		except EmptyPage:
			listNews = paginator.page(paginator.num_pages)


		tag_cloud = self.model.tags.most_common()[:10]


		context = {
			'news':listNews,
			'title': category.title,
			'tag_cloud':tag_cloud,
		}
		return render(request, 'list_view.html', context)

class NewsListView(ListView):

	model = News

	def get(self, request):

		listNews = self.model.objects.filter(publish=True, publisdDate__lt=timezone.now()).order_by('-publisdDate')

		page = request.GET.get('page', 1)

		paginator = Paginator(listNews, NUMBER_PAGE)

		try:
			listNews = paginator.page(page)
		except PageNotAnInteger:
			listNews = paginator.page(1)
		except EmptyPage:
			listNews = paginator.page(paginator.num_pages)


		tag_cloud = self.model.tags.most_common()[:10]

		context = {
			'news':listNews,
			'title': 'Последние новости',
			'tag_cloud':tag_cloud,
			'paginator': paginator,
		}
		return render(request, 'list_view.html', context)


class TagNewsListView(ListView):

	model = News

	def get(self, request, tag_slug):

		tag = Tag.objects.get(slug=tag_slug)

		listNews = get_list_or_404(News.objects.filter(tags__slug__in=[tag_slug], publish=True, publisdDate__lt=timezone.now()).order_by('-publisdDate'))

		page = request.GET.get('page', 1)

		paginator = Paginator(listNews, NUMBER_PAGE)

		try:
			listNews = paginator.page(page)
		except PageNotAnInteger:
			listNews = paginator.page(1)
		except EmptyPage:
			listNews = paginator.page(paginator.num_pages)
		

		tag_cloud = self.model.tags.most_common()[:10]


		context = {
			'news':listNews,
			'title': tag.name,
			'tag_cloud':tag_cloud,
		}
		return render(request, 'list_view.html', context)

class NewsDetailView(DetailView):

	model = News

	def get(self, request, id, slug):

		new = get_object_or_404(News, pk=id, slug=slug)

		tag_cloud = self.model.tags.most_common()[:12]

		context = {
			'new':new,
			'tag_cloud':tag_cloud,
		}

		return render(request, 'news_detail.html', context)


class IndexView(ListView):

	model = News

	def get(self, request):

		topNews = News.objects.filter(publish=True, topNews=True).order_by('-publisdDate')

		OneMainNew = topNews[0]

		topNews = topNews[1:11]

		listNews = News.objects.filter(publish=True, topNews=False).order_by('-publisdDate')

		listNews = listNews[:12]

		chairman = deputat.objects.get(chairman=True)

		context = {
			'MainNew': OneMainNew,
			'topNews':topNews,
			'listNews':listNews,
			'chairman':chairman,
		}

		return render(request, 'index.html', context)