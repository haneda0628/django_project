"""project URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login,logout

from . import views

urlpatterns = [
    url(r'^login/$', login,{'template_name': 'accounts/login.html'},name='login'),
    url(r'^current_datetime/$', views.current_datetime, name='current_datetime'),
    url(r'^add_company/(?P<company_name>)/(?P<post_number>)/(?P<address>)/$', views.add_company, name='add_company'),
    url(r'^logout/$', logout, name='logout')
]
