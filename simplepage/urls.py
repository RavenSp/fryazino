from django.urls import path, include
from django.views.generic.base import RedirectView

from . import views


urlpatterns = [
	path('doc-autocomplete/', views.DocumentsAutocompile.as_view(), name='doc-autocomplete'),
	path('<slug:pg>/', views.PageView.as_view(), name='simplePage'),
	
	]