from django.urls import path
from .views import GarageList, VoitureList, CleList

urlpatterns = [
    path('garages/', GarageList.as_view(), name='garage_list'),
    path('voitures/', VoitureList.as_view(), name='voiture_list'),
    path('cles/', CleList.as_view(), name='cle_list'),
]


