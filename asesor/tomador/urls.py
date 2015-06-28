from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index , name='index'),
    url(r'^nocongruencia/',views.nocongruencia, name='nocongruencia'),
    url(r'^respuesta/',views.nocongruencia, name='respuesta'),
]