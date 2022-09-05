"""sok_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.views.generic import RedirectView

# from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic.base import TemplateView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from . import settings
from django.conf.urls.static import static
from django.views.static import serve
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("gallery/", views.gallery, name="gallery"),
    path("gallery/<str:folder>", views.gallery, name="gallery"),
    path("image/<str:file>",views.image, name="image"),
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("img/favicon.ico")),
    ),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += [
        re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
        #re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    ]
