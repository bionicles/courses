from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses/destroy/(?P<id>\d+)', views.confirm),
    url(r'^courses/destroy/nuke/(?P<id>\d+)', views.destroy),
    url(r'^add', views.add)
]
