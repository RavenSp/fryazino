from django.urls import path, include
from django.views.generic.base import RedirectView
from taggit.models import Tag

from . import views


urlpatterns = [

	path('tag<slug:tag_slug>/', views.TagNewsListView.as_view(), name='tag_path'),
	path('category/<str:cat>/', views.CategoryNewsListView.as_view(), name='CategoryList'),
	path('category/', RedirectView.as_view(url='/news/')),
	path('', views.NewsListView.as_view(), name='AllNewsList'),
	path('<int:id>-<slug:slug>/', views.NewsDetailView.as_view(), name='NewDetail'),
	
]