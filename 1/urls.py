from django.conf.urls import include, url, patterns
from django.contrib import admin
from tastypie.api import Api
from .api import EntryResource

__author__ = 'Otto'


v1_api = Api(api_name='v1')
v1_api.register(EntryResource())

urlpatterns = patterns('',

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^customer_details/', include('customer_care.urls', namespace="customer_details")),
                       url(r'^api/', include(v1_api.urls)),

                       )
