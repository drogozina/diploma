"""DIPLOMA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from test3 import views
admin.autodiscover()

urlpatterns = [
    #
    url(r'^admin', include(admin.site.urls)),
    url(r'^getinfo/', views.info, name="info"),
    # url(r'^sendform/', views.sendForm, name="sendForm"),
    url(r'^create/(?P<pk>[0-9]+)/$', views.create, name="create"),
    url(r'^finish/(?P<pk>[0-9]+)/$', views.finish, name="finish"),
    url(r'^download/(?P<pk>[0-9]+)/$', views.fileDown, name="download"),
    url(r'', views.root, name="root"),
]
