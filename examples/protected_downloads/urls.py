#from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('download.urls')),
    (r'^admin/', include(admin.site.urls)),
)
