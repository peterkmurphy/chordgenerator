from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'chordgenerator.views.index'),    
)
