from django.urls import path, include
from django.views.generic.base import RedirectView

from .views import DeputatList


urlpatterns = [
	path('list/', DeputatList.as_view(), name='deputat_list'),
]