from django.shortcuts import render

from .models import allSitesMenu
# Create your views here.

def allSitesList(request):

	if request.method == 'GET':

		siteList = allSitesMenu.objects.filter(active=True)

		return render(request, 'all_sites.html', {'sitesList':siteList})