from django.db import models

# Create your models here.
class Client(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50 )
    tel = models.CharField(max_length=11)
    email = models.EmailField( max_length=254)
    adresse = models.TextField()
    localisation =models.TextField()
    


    def __str__(self):
        return 


class Livreur(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50 )
    tel = models.CharField(max_length=11)
    email = models.EmailField( max_length=254)
    def __str__(self):
        return 


class Gestionnaire(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50 )
    tel = models.CharField(max_length=11)
    email = models.EmailField( max_length=254)
    def __str__(self):
        return 


class Commande(models.Model):
    

    def __str__(self):
        return 


class Livraison(models.Model):
    

    def __str__(self):
        return 

 
class Attribution(models.Model):
    

    def __str__(self):
        return 
