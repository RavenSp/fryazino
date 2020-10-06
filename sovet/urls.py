from django.urls import path, include
from django.views.generic.base import RedirectView

from .views import DeputatList, DeputatView


urlpatterns = [
	path('deputat/<int:deputat>', DeputatView.as_view(), name='deputat_detail'),
	path('list/', DeputatList.as_view(), name='deputat_list'),
]