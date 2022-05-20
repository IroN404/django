from django.db import models

# Create your models here.

class telephone(models.Model):
    modele = models.CharField(max_length=100)
    stockage = models.integer_field(blank=False)
    date_sortie = models.DateField(blank=True, null=True)
    details = models.text_field(blank=True, null=True)

    def __str__(self):
        chaine = f"{self.modele} {self.stockage} {self.date_sortie} {self.details}"
        return chaine

class categorie(models.model):
    nom = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.nom