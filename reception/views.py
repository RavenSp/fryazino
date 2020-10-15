from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
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

	def post(self, request, rec):

		form = ApperalForm(request.POST, request.FILES)

		if form.is_valid():

			app = form.save(commit=False)

			app.ipaddres = request.META.get("REMOTE_ADDR")

			app.recipient = recipient.objects.get(slug=rec)

			app.save()

			context = {
				'number': app.addzero,
				'numdate':app.created,
				'email': app.email,
			}

			return render(request, 'reception_done.html', context)


class Reception(View):

	def get(self, request):

		context = {
			'title':'законодательство',
		}

		return render(request, 'reception.html', context)