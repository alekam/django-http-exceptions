from django.conf.urls import include, url

from .views import fail_view, success_view


urlpatterns = [
    url(r'^success/$', success_view, name='success_view'),
    url(r'^fail/$', fail_view, name='fail_view'),
]
