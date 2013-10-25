from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('pestileaks.views',
    url(r'^$', 'index', name='index'),
    url(r'^service/?$', 'service', name='service'),
    (r'^admin/', include(admin.site.urls)),
)
