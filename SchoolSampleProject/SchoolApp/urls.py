from django.urls import re_path
from SchoolApp import views


urlpatterns = [
    re_path(r'^school$', views.schoolApi),
    re_path(r'^school/([0-9]+)$', views.schoolApi),
]
