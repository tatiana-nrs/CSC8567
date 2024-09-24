from rest_framework import serializers
from public.models import Garage, Voiture, Cle

class CleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cle
        fields = ['etat_pret', 'date_pret', 'date_rendu']

class VoitureSerializer(serializers.ModelSerializer):
    cle = CleSerializer()

    class Meta:
        model = Voiture
        fields = ['marque', 'modele', 'immatriculation', 'cle']

class GarageSerializer(serializers.ModelSerializer):
    voitures = VoitureSerializer(many=True, source='voiture_set')

    class Meta:
        model = Garage
        fields = ['nom', 'voitures']

