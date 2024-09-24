from rest_framework import generics
from public.models import Garage, Voiture, Cle
from .serializers import GarageSerializer, VoitureSerializer, CleSerializer

class GarageList(generics.ListCreateAPIView):
    queryset = Garage.objects.all()
    serializer_class = GarageSerializer

class VoitureList(generics.ListCreateAPIView):
    queryset = Voiture.objects.all()
    serializer_class = VoitureSerializer

class CleList(generics.ListCreateAPIView):
    queryset = Cle.objects.all()
    serializer_class = CleSerializer




