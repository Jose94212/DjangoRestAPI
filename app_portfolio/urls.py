from django.conf.urls import url
from app_portfolio import views
from django.urls import path



urlpatterns=[
    path('', views.index),
    path('apple/',views.view_apple),
    path('company/new',views.post_new,name='post_new'),
    path('company/<int:pk>/',views.post_detail,name='post_detail'),
    path('company/<str:company_name>',views.view_company_name), 
]