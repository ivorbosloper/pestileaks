from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('pestileaks.views',
    url(r'^$', 'index', name='index'),
    url(r'^app/?$', 'app', name='app'),
    url(r'^contribute/?$', 'contribute', name='contribute'),
    url(r'^overview/?$', 'overview', name='overview'),
    url(r'^motivation/?$', 'motivation', name='motivation'),

    url(r'^service/?$', 'service', name='service'),
    url(r'^gewassen.json/?$', 'gewassen', name='gewassen'),
    
    (r'^admin/', include(admin.site.urls)),
)
