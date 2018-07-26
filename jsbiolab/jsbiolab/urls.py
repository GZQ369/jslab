"""jsbiolab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from jslab.views import homepage,index,index2,index3,news,services,connect,detail

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',index),
    url(r'^index$',homepage),
    url(r'^index2$',index2),
    url(r'^index3$',index3),
    url(r'^news$',news),
    url(r'^services$',services),
    url(r'^connect$',connect),
    url(r'^detail/(.+)$',detail),
]
