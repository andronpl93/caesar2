from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(views,
    url(r'^$', views.start, name='start' ),
    url(r'^decoder/$', views.decoder),
    url(r'^encoder/$', views.encoder),
    url(r'^vanga/$', views.vanga),

)
	