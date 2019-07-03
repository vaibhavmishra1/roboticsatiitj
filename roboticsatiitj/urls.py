"""roboticsatiitj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from registration import views as stores_views
from django.contrib.auth import views as auth_views
from django.conf.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',stores_views.HomeCreateView.as_view(),name='home'),
 	url(r'^accounts/', include('allauth.urls')),
 	url(r'^profile/(?P<pk>[0-9]+)/$',stores_views.UserProfileView.as_view(), name='edit'),
    url(r'^myprojects/$',stores_views.UserProjectsView.as_view(), name='myprojects'),
	url(r'^myprojects/add/$',stores_views.ProjectCreateView.as_view(), name='addproject'),

    url(r'^projects/$',stores_views.GeneralProjectsView.as_view(), name='allprojects'),
]
