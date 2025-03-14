from django.urls import path

from .api import properties_list


urlpatterns = [
    path('', properties_list, name='api_properties_list'),
]
