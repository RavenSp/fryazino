from django.urls import path, include
from django.views.generic.base import RedirectView

from .views import DeputatList, DeputatView, PartyDetail


urlpatterns = [
	path('deputat/<int:deputat>', DeputatView.as_view(), name='deputat_detail'),
	path('list/', DeputatList.as_view(), name='deputat_list'),
	path('party/<slug:part>', PartyDetail.as_view(), name='party_detail'),
]