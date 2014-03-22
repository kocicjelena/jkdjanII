from django.conf.urls import patterns, include, url
from Blog import views
from Blog.views import posts, search, searchform, i
from django.conf.urls import patterns
from .views import AboutView
from django.conf.urls import patterns
from .views import BookListView
from django.conf.urls import patterns
from .views import MyView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^year_archive/(?P<year>\d{4})/$', views.year_archive),
	#url(r'^foo/$', views.foo_view),
    #url(r'^bar/$', views.bar_view),
	#url(r'^blog/entries/$', views.entry_list),
	url(r'^about/', MyView.as_view()),
	url(r'^books/$', BookListView.as_view()),
	#url(r'^about/', AboutView.as_view()),
	url(r'^posts/$', views.posts),
	url(r'^searchform/$', views.searchform),
	url(r'^search/$', views.search),
	url(r'^i/$', views.i),
	#url(r'^blogs_of_author/$', views.blogs_of_author),
	#url(r'^fo/$', views.fo),
	#url(r'^f/$', views.f),
	#url(r'^blog/edit/(?P<id>.*)$', 'views.edit_view', name='item_edit'),
    #url(r'^blog/remove/(?P<id>.*)$', 'views.remove_view', name='item_remove'),
    # ...
	)