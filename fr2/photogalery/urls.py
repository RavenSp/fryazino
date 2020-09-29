from django.urls import path, include
from django.views.generic.base import RedirectView


from . import views


urlpatterns = [
	path('', views.GaleryListView.as_view(), name='galery-list'),
	path('<slug:url>', views.GaleryDetailView.as_view(), name='galery-detail'),
	]