from django.urls import path, include
from django.views.generic.base import RedirectView


from . import views


urlpatterns = [
	
	path('', views.Reception.as_view(), name='reception'),
	path('<slug:rec>', views.ReceptionGlava.as_view(), name='reception_glava'),

	
]