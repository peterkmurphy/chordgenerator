# Deprecated and removed in Django 1.6:
# from django.conf.urls.defaults import *

from django.conf.urls import url, include
from chordgenerator.views import index as viewindex

urlpatterns =[ url(r'^$', viewindex)]
