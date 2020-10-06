from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView
from django.views import View
from .models import party, okrug, deputat, commision
# Create your views here.

class DeputatList(ListView):

    model = deputat

    def get(self, request, *args, **kwargs):

        deps = self.model.objects.all().order_by('okrug')

        title = 'Совет депутатов городского округа Фрязино'

        chairman = deps.filter(chairman=True)

        vicechairman = deps.filter(vicechairman=True)

        context = {
            'title':title,
            'deps': deps,
            'chairman': chairman[0],
            'vicechairman': vicechairman[0],
        }

        return render(request, 'deputatList.html', context)

class DeputatView(DetailView):

    model = deputat

    def get(self, request, deputat):

        dep = get_object_or_404(self.model, id=deputat)

        context = {
            'deputat':dep,
        }

        return render(request, 'deputatDetail.html', context)


class OkrugDetail(DetailView):

    model = okrug

    def get(self, request, okrug):

        okr = get_object_or_404(self.model, slug=okrug)

        deps = deputat.objects.filter(okrug=okrug)

        context = {
            'okrug': okr,
            'deps': deps,
        }

        return render(request, 'Okrug.html', context)

class CommissionList(ListView):

    model = commision

    def get(self, request):

        comms = commision.objects.all()

        context = {
        	'commisions':comms,
        }

        return render(request, 'commissionList.html', context)

class CommissionDeatails(DetailView):

	model = commision 

	def get(self, request, slug):

		com = get_object_or_404(commision, slug=slug)

		context = {
			'comm':comm,
		}

		return render(request, 'commissionDetails.html', context)
