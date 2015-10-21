from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^signup$', SignUp, name='signup'),
    url(r'^activate/(?P<user>[\w\.]+)/(?P<act>\w+)$', Activate, name='registration_activate'),
    url(r'^registration_complete$',Reg_Complete,name='reg_complete'),
    url(r'^activation_success$',Activ_succ,name='activ_success'),
    url(r'^log_in$',Login,name='login'),
    url(r'^dashboard$',Dashboard,name='dashboard'),
    url(r'^log_out$',Logout,name='logout'),
    url(r'^forgot_pw$',Forgot_PW, name='forgot_pw'),
    url(r'^new_pw/(?P<user>[\w\.]+)/(?P<act>\w+)$', New_PW, name='new_pw'),

)
