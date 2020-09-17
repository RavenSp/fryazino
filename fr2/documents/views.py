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

		docs = Documents.objects.filter(publish=True, publishDate__lt=timezone.now()).order_by('-publishDate')

		page = request.GET.get('page', 1)

		paginator = Paginator(docs, NUMBER_PAGE)

		try:
			docs = paginator.page(page)
		except PageNotAnInteger:
			docs = paginator.page(1)
		except EmptyPage:
			docs = paginator.page(paginator.num_pages)

		context = {
			'docs':docs,
		}

		return render(request, 'documentsList.html', context)

class documentsDetail(DetailView):

	model = Documents

	def get(self, request, slug):

		doc = get_object_or_404(Documents, slug=slug, publish=True)

		context = {
			'doc':doc,
		}

		return render(request, 'documentsDetail.html', context)