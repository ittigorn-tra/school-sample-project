from django.urls import re_path, path
from SchoolApp import views


urlpatterns = [
    path('school/', views.schoolApi),
    re_path(r'^school/([0-9]+)$', views.schoolApi),
]
