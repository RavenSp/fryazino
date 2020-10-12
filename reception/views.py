from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView, View
from django.views import View
from .models import theme, recipient, apperal
from .forms import ApperalForm

# Create your views here.
class ReceptionGlava(View):

	models = apperal

	form = ApperalForm()

	def get(self, request, rec=None):


		if rec == None:

			context = {
				'title': 'законодательство',
			}

			return render(request, 'reception.html', context)


		rcpn = get_object_or_404(recipient, slug=rec)

		title = rcpn.title

		context = {
			'form': self.form,
			'title': title
		}

		

		return render(request, 'reception_glava.html', context)


class Reception(View):

	def get(self, request):

		context = {
			'title':'законодательство',
		}

		return render(request, 'reception.html', context)