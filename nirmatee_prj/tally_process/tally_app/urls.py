from django.urls import path
from .views import process_xml_api

urlpatterns = [
    path('processing/', process_xml_api),
]
