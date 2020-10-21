from itertools import chain
 
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import View

from documents.models import Documents
from news.models import News
from simplepage.models import Page
from sovet.models import deputat, party


class ESearchView(View):

	template_name = 'search.html'

	def get(self, request, *args, **kwargs):

		context = {}

		q = request.GET.get('q')

		if q:

			query_sets = []

			query_sets.append(News.search(q))
			query_sets.append(Documents.search(q))
			query_sets.append(Page.search(q))
			query_sets.append(deputat.search(q))
			query_sets.append(party.search(q))

			final_set = list(chain(*query_sets))

			final_set.sort(key=lambda x: x.pub_date(), reverse=True)

			context['last_question'] = '?q=%s' % q
			context['object_list'] = final_set
			context['title'] = q

		return render(request=request, template_name=self.template_name, context=context)
