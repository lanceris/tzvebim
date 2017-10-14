from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', views.log_out, name='logout'),
]