from django.db import models

class Garage(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom

    class Meta:
        app_label = 'public'

class Voiture(models.Model):
    couleur = models.CharField(max_length=30)
    immatriculation = models.CharField(max_length=9)
    marque = models.CharField(max_length=30)
    modele = models.CharField(max_length=30)
    garage = models.ForeignKey(Garage, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.marque} {self.modele} - {self.immatriculation}"
    
    class Meta:
        app_label = 'public'

class Cle(models.Model):
    etat_pret = models.BooleanField(default=False)
    date_pret = models.DateField(null=True, blank=True)
    date_rendu = models.DateField(null=True, blank=True)
    voiture = models.OneToOneField(Voiture, on_delete=models.CASCADE)

    def __str__(self):
        return f"Clé de {self.voiture}"
    
    class Meta:
        app_label = 'public'


