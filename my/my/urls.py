from django.conf.urls import patterns, include, url
from django.contrib import admin

from book.views import index,information,addbook,search,addauthor,update

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', index),
    url(r'^information/(.+)/$', information),
    url(r'^addbook/$', addbook),
    url(r'^search/$', search),
    url(r'^addauthor/$', addauthor),
    url(r'^update/(.+)/$', update),
    url(r'^update/$', update), 
)
