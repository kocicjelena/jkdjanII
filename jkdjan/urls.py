from django.conf.urls import patterns, include, url
from Blog import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jkdjan.views.home', name='home'),
    # url(r'^jkdjan/', include('jkdjan.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'jkdjan.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('Blog.urls')),
)
