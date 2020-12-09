from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Documents, DocsAuthor, DocType, DocCategory
from .forms import DocFilter
from menu.models import Menu
# Create your views here.

######### Настройка кол-ва документов на странице ############
NUMBER_PAGE = 50
##############################################################

class documetns(ListView):

	model = Documents

	def get(self, request):



		if request.GET.get('author', '') and request.GET.get('typedoc', ''):

			author = request.GET.get('author', '')
			typedoc = request.GET.get('typedoc', '')

			docs = get_list_or_404(Documents.objects.filter(publish=True, publishDate__lt=timezone.now(), Author__id = author, TypeDoc__id = typedoc).order_by('-publishDate'))

			title = '%s | %s' % (docs[0].TypeDoc.title, docs[0].Author.title)



		elif request.GET.get('author', ''):

			author = request.GET.get('author', '')

			docs = get_list_or_404(Documents.objects.filter(publish=True, publishDate__lt=timezone.now(), Author__id = author).order_by('-publishDate'))

			title = 'Документы | %s' % docs[0].Author.title


		elif request.GET.get('typedoc', ''):

			typedoc = request.GET.get('typedoc', '')

			docs = get_list_or_404(Documents.objects.filter(publish=True, publishDate__lt=timezone.now(), TypeDoc__id = typedoc).order_by('-publishDate'))

			title = '%s' % docs[0].TypeDoc.title

		else:

			docs = Documents.objects.filter(publish=True, publishDate__lt=timezone.now()).order_by('-publishDate')

			title = 'Нормативные документы'

		page = request.GET.get('page', 1)

		paginator = Paginator(docs, NUMBER_PAGE)

		try:
			docs = paginator.page(page)
		except PageNotAnInteger:
			docs = paginator.page(1)
		except EmptyPage:
			docs = paginator.page(paginator.num_pages)

		submenu = DocCategory.objects.filter(active=True)

		form = DocFilter()		


		context = {
			'title': title,
			'submenu':submenu,
			'docs':docs,
			'form':form,
		}

		for i in request.GET:

			print(i, request.GET[i])

		return render(request, 'documentsList.html', context)

	def post(self, request):

		form = DocFilter(request.POST)

		docs = Documents.objects.filter(publish=True, publishDate__lt=timezone.now()).order_by('-publishDate')

		if form.is_valid():
			
			if form.cleaned_data['number']:

				docs = docs.filter(number=form.cleaned_data['number'])

			if form.cleaned_data['author']:

				docs = docs.filter(Author=form.cleaned_data['author'])

			if form.cleaned_data['category']:

				docs = docs.filter(DocCategory=form.cleaned_data['category'])

			if form.cleaned_data['dateStart']:

				docs = docs.filter(docDate__gte=form.cleaned_data['dateStart'])

			if form.cleaned_data['dateEnd']:

				docs = docs.filter(docDate__lte=form.cleaned_data['dateEnd'])
			




		else:
			print('not valid')

		title = 'Нормативные документы'
		submenu = DocCategory.objects.filter(active=True)

		context = {
			'title': title,
			'submenu':submenu,
			'docs':docs,
			'form':form,
		}

		return render(request, 'documentsList.html', context)

class documentsDetail(DetailView):

	model = Documents

	def get(self, request, slug):

		doc = get_object_or_404(Documents, slug=slug, publish=True, publishDate__lt=timezone.now())


		context = {
			
			'doc':doc,
		}

		return render(request, 'documentsDetail.html', context)


class documentsAutorList(ListView):

	model = Documents

	def get(self, request, slug):

		docs = get_list_or_404(Documents, Author__slug=slug, publish=True, publishDate__lt=timezone.now())



		page = request.GET.get('page', 1)

		paginator = Paginator(docs, NUMBER_PAGE)

		try:
			docs = paginator.page(page)
		except PageNotAnInteger:
			docs = paginator.page(1)
		except EmptyPage:
			docs = paginator.page(paginator.num_pages)

		context = {
			'title':'%s  | Документы' % docs[0].Author.title,
			'docs':docs,
		}

		return render(request, 'documentsList.html', context)


class documentsCateforyList(ListView):

	model = Documents

	def get(self, request, category):

		cat = get_object_or_404(DocCategory, slug=category, active=True)

		docs = Documents.objects.filter(DocCategory=cat, publish=True, publishDate__lt=timezone.now())

		submenu = DocCategory.objects.filter(active=True)

		page = request.GET.get('page', 1)

		paginator = Paginator(docs, NUMBER_PAGE)

		try:
			docs = paginator.page(page)
		except PageNotAnInteger:
			docs = paginator.page(1)
		except EmptyPage:
			docs = paginator.page(paginator.num_pages)

		submenu = DocCategory.objects.filter(active=True)

		context = {

			'category': cat,
			'submenu':submenu,
			'docList': docs,

		}

		return render(request, 'docCategoryList.html', context)



