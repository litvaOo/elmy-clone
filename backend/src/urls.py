"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from jobs.views import home_page, job_list, job_redirect, job_type_complete, book_page, bookings
from accounts.views import provider_page, signup_view, login_view, logout_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page, name='home'),
    url(r'^search/(?P<job_type>[\w\-]+)/(?P<city>[\w\-]+)$', job_list, name='job_list'),
    url(r'^provider/(?P<pk>[0-9]+)/$', provider_page, name='provider_page'),
    url(r'^job-redirect/$', job_redirect, name='job-redirect'),
    url(r'^ajax/login/$', login_view, name='login'),
    url(r'^ajax/signup/$', signup_view, name='signup'),
    url(r'^ajax/logout/$', logout_view, name='logout'),
    url(r'^ajax/job-type/$', job_type_complete, name='job_type_complete'),
    url(r'^book/(?P<pk>[0-9]+)/$', book_page, name='book_page'),
    url(r'^bookings/$', bookings, name='bookings')
]
