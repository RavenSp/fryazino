from itertools import chain
 
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import View

from documents.models import Documents
from news.models import News
from simplepage.models import Page
from sovet.models import deputat, party, commision


class ESearchView(View):

	template_name = 'search.html'

	def get(self, request, *args, **kwargs):

		context = {}

		q = request.GET.get('q')

		if q:

			query_sets = []

			query_sets.append(News.search(q))

			final_set = list(chain(*query_sets))

			final_set.sort(key=lambda x: x.publisdDate, reverse=True)

			context['last_question'] = '?q=%s' % q
			context['object_list'] = final_set

		return render(request=request, template_name=self.template_name, context=context)
