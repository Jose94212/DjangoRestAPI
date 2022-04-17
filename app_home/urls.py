from django.conf.urls import url
from app_home import views
from django.urls import path

urlpatterns=[
    path('',views.home)
]