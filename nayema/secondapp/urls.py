from django.urls import path
from . import views

urlpatterns = [
    path('bc/', views.Beautiful_Color),
    path('sb/', views.Sirat_Book),

]