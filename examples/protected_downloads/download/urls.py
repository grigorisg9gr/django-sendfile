#from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url # django 1.6

from .views import download, download_list

urlpatterns = patterns('',
    url(r'^$', download_list),
    url(r'(?P<download_id>\d+)/$', download, name='download'),
)
