from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('voitures/', views.list_cars, name='list_cars'), 
    path('voitures/<int:voiture_id>/', views.detail_cars, name='detail_cars'),
    path('cles/', views.list_keys, name='list_keys'),
]
