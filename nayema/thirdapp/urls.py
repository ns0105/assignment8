from django.urls import path
from . import views

urlpatterns = [
    path('cn/', views.Class_Number),
    path('ct/', views.Class_Time),

]
