from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^pholius/', include('pholius.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),

    #date based urls
    (r'^$', 'pholius.core.views.index'),
    (r'^(?P<year>\d{4})/$', 'pholius.core.views.year_archive'),
    (r'^(?P<year>\d{4})/(?P<month>\d{2})/$', 'pholius.core.views.month_archive'),
    (r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', 'pholius.core.day_archive'),
    (r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<title_slug>\w+)/$', 'pholius.core.content_detail'),
    #taxonomy based urls
    (r'^(?P<taxonomy_type>\w+)/$', 'pholius.core.views.taxonomies'),
    (r'^(?P<taxonomy_type>\w+)/(?P<taxnomy_slug>\w+)/$', 'pholius.core.views.taxonomy_archive'),
    #author based urls
    (r'^authors/$', 'pholius.core.views.authors'),
    (r'^authors/(?P<author_slug>\w+)/$', 'pholius.core.views.author'),
    #static page urls
    (r'^(?P<page_slug>\w+)/$', 'pholius.core.views.page'),

)
