import imp
from django.conf import urls
from django.urls import URLPattern
from django.urls import path
from app_simpleform import views

urlpatterns=[
    path('',views.student),
    path('studinfo/',views.student_retrieve),
    path('studjson/<int:pk>',views.student_detail),
    path('students/',views.student_list),
    path('studentapi/',views.student_api)
    ]
