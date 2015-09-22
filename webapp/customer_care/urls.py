from django.conf.urls import url, patterns

__author__ = 'Otto'

urlpatterns = patterns('',

                       url(r'^index$', 'customer_care.views.index', name='index'),
                       url(r'^register$', 'customer_care.views.customer_register_view', name='register'),
                       url(r'^user_login/(?P<activation_key>\w+)/$', 'customer_care.views.user_login_view',
                           name='user_login'),
                       url(r'^auth/$', 'customer_care.views.authenticate_view', name='auth'),
                       url(r'^loggedin$', 'customer_care.views.loggedin_view', name='loggedin'),
                       url(r'^logout$', 'customer_care.views.logout_view', name='logout'),
                       url(r'^activate$', 'customer_care.views.activate_view', name='activate'),

                       )