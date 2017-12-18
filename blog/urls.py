from django.conf.urls import url
from . import viewss
urlpatterns = [
    url(r'^$', viewss.post_list, name='post_list'),
]