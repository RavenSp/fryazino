from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import TypeMUP, ListMUP
# Create your views here.

class TypeMupList(ListView):

	model = TypeMUP



	def get(self, request):

		m_list = TypeMUP.objects.all()

		title = 'Муниципальные учреждения городского округа Фрязино'

		context = {
			'm_list': m_list,
			'title':title,
		}

		return render(request, 'list_mup.html', context)