from __future__ import unicode_literals, absolute_import
from django.conf.urls import include, url
from rest_framework.authtoken import views

from farm_api.views import fetch_villages

urlpatterns = [
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^fetch-villages/$', fetch_villages)
]
