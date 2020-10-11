from django.urls import path, include
from django.views.generic.base import RedirectView

from .views import DeputatList, DeputatView, PartyDetail, CommissionList


urlpatterns = [
	path('deputat/<int:deputat>', DeputatView.as_view(), name='deputat_detail'),
	path('', DeputatList.as_view(), name='deputat_list'),
	path('party/<slug:part>', PartyDetail.as_view(), name='party_detail'),
	path('comission/', CommissionList.as_view(), name='comission_list'),
]