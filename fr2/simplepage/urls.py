from django.urls import path, include
from django.views.generic.base import RedirectView

from . import views


urlpatterns = [
	path('<slug:pg>/', views.PageView.as_view(), name='simplePage'),
	]