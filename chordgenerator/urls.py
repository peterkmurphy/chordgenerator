# Deprecated and removed in Django 1.6: 
# from django.conf.urls.defaults import *
from django.conf.urls import *

urlpatterns = patterns('',
    (r'^$', 'chordgenerator.views.index'),    
)
