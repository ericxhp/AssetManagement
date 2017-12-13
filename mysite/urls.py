"""mysite URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from tutorial.views import people
from equipment.views import FilteredAssetListView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)), 

    url(r'^blog/', include('blog.urls',
        namespace='blog',
        app_name='blog')),
    url(r'^people/', people),
    # url(r'^asset/', asset),
    # url(r'^assetfilter$', asset_filter),
    #url(r'^bootstrap/$', bootstrap, name='bootstrap'),
    url(r'^asset/$', FilteredAssetListView.as_view(), name='filtertableview'),


]