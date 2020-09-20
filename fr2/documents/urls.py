from django.urls import path, include
from django.views.generic.base import RedirectView

from . import views


urlpatterns = [
	path('', views.documetns.as_view(), name='all_documents'),
	path('<slug:slug>/', views.documentsDetail.as_view(), name='docs_detail'),
	path('author/<slug:slug>', views.documentsAutorList.as_view(), name='docs-author-list'),
	
]