from django.urls import path, re_path

from SchoolApp import views

urlpatterns = [
    path('schools', views.schoolApi),
    re_path(r'^schools/([0-9]+)$', views.schoolApi),

    path('students', views.studentApi),
    re_path(r'^students/(\w{1,20})$', views.studentApi),

    re_path(r'^schools/([0-9]+)/students$', views.schoolStudentsApi),
]
