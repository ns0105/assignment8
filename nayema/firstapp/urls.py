from django.urls import path
from . import views

urlpatterns = [
    path('', views.app),
    path('mi/', views.My_Identity),
    path('mh/', views.My_Hobby),

]
