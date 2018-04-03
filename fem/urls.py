from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ajax/calculate_temperatures/$', views.calculate_temperatures, name='calculate_temperatures'),
]