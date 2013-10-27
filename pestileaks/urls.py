from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('pestileaks.views',
    url(r'^$', 'index', name='index'),
    url(r'^service/?$', 'service', name='service'),
    url(r'^app/?$', 'app', name='app'),
    url(r'^contribute/?$', 'contribute', name='contribute'),
    url(r'^overview/?$', 'overview', name='overview'),
    url(r'^motivation/?$', 'motivation', name='motivation'),
    (r'^admin/', include(admin.site.urls)),
)
