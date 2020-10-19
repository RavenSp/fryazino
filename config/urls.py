"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from news.views import IndexView
from menu.views import allSitesList
from search.views import ESearchView 

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
	path('news/', include('news.urls'), name='news'),
	path('documents/', include('documents.urls'), name='documents'),
	path('sovet/', include('sovet.urls'), name='sovet'),
    path('catalog/', include('catalog.urls'), name='catalog'),
    path('galery/', include('photogalery.urls'), name='galery'),
    path('reception/', include('reception.urls'), name='reception'),
    path('all-sites/', allSitesList, name='all_sites'),
    path('search/', ESearchView.as_view(), name='search'),


    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('taggit_autosuggest/', include('taggit_autosuggest.urls')),
    path('', include('simplepage.urls'), name='simplepage'),
    path('captcha/', include('captcha.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls)),] + urlpatterns

