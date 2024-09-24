from django.shortcuts import render
from .models import Garage, Voiture, Cle

def list_cars(request):
    garages = Garage.objects.all()
    return render(request, 'list_cars.html', {'garages': garages})

def detail_cars(request, voiture_id):
    voiture = Voiture.objects.get(id=voiture_id)
    return render(request, 'detail_cars.html', {'voiture': voiture})

def list_keys(request):
    all_keys = Cle.objects.all()
    # Filtre les clés disponibles et utilisées
    available_keys = all_keys.filter(etat_pret=False)  # false= libre
    used_keys = all_keys.filter(etat_pret=True)  # true= utilisé
    
    return render(request, 'list_keys.html', {
        'available_keys': available_keys,
        'used_keys': used_keys,
    })

def home(request):
    return render(request, 'index.html')
