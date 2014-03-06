from django.conf.urls import patterns, include, url

from django.contrib import admin
from tastypie.api import Api
from pestileaks.api import CtgbToelatingResource, CtgbWerkzamestofResource, CtgbHoeveelheidResource, GewasResource, ToepassingsMethodeResource,\
    MiddelResource, AantastingResource, GebruiksRegelResource
admin.autodiscover()

urlpatterns = patterns('pestileaks.views',
    url(r'^$', 'index', name='index'),
    url(r'^app/?$', 'app', name='app'),
    url(r'^contribute/?$', 'contribute', name='contribute'),
    url(r'^overview/?$', 'overview', name='overview'),
    url(r'^motivation/?$', 'motivation', name='motivation'),

    url(r'^service/?$', 'service', name='service'),
    url(r'^gewassen.json/?$', 'gewassen', name='gewassen'),
    url(r'^middelen.json/?$', 'middelen', name='middelen'),
    
    (r'^admin/', include(admin.site.urls)),
)

v1_api = Api(api_name='api')
v1_api.register(CtgbToelatingResource())
v1_api.register(CtgbWerkzamestofResource())
v1_api.register(CtgbHoeveelheidResource())
v1_api.register(GewasResource())
v1_api.register(ToepassingsMethodeResource())
v1_api.register(MiddelResource())
v1_api.register(AantastingResource())
v1_api.register(GebruiksRegelResource())
urlpatterns += v1_api.urls
