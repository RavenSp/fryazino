from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Documents, DocsAuthor, DocType
# Create your views here.

######### Настройка кол-ва документов на странице ############
NUMBER_PAGE = 20
##############################################################

class documetns(ListView):

	model = Documents

	def get(self, request):

		if request.GET.get('author', '') and request.GET.get('typedoc', ''):

			author = request.GET.get('author', '')
			typedoc = request.GET.get('typedoc', '')

			docs = get_list_or_404(Documents.objects.filter(publish=True, publishDate__lt=timezone.now(), Author__slug = author, TypeDoc__slug = typedoc).order_by('-publishDate'))

			title = '%s | %s' % (docs[0].TypeDoc.title, docs[0].Author.title)



		elif request.GET.get('author', ''):

			author = request.GET.get('author', '')

			docs = get_list_or_404(Documents.objects.filter(publish=True, publishDate__lt=timezone.now(), Author__slug = author).order_by('-publishDate'))

			title = 'Документы | %s' % docs[0].Author.title


		elif request.GET.get('typedoc', ''):

			typedoc = request.GET.get('typedoc', '')

			docs = get_list_or_404(Documents.objects.filter(publish=True, publishDate__lt=timezone.now(), TypeDoc__slug = typedoc).order_by('-publishDate'))

			title = '%s' % docs[0].TypeDoc.title

		else:

			docs = Documents.objects.filter(publish=True, publishDate__lt=timezone.now()).order_by('-publishDate')

			title = 'Документы'

		page = request.GET.get('page', 1)

		paginator = Paginator(docs, NUMBER_PAGE)

		try:
			docs = paginator.page(page)
		except PageNotAnInteger:
			docs = paginator.page(1)
		except EmptyPage:
			docs = paginator.page(paginator.num_pages)

		context = {
			'title': title,
			'docs':docs,
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
