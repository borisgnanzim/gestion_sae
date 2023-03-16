from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User 


# Create your models here.
class Client(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50 )
    tel = models.CharField(max_length=15)
    email = models.EmailField( max_length=254)
    adresse = models.TextField()
    localisation =models.TextField()
    


    def __str__(self):
        return self.nom


class Livreur(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50 )
    tel = models.CharField(max_length=11)
    email = models.EmailField( max_length=254,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE ,null=True)
    def __str__(self):
        return self.nom


class Gestionnaire(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50 )
    tel = models.CharField(max_length=11)
    email = models.EmailField( max_length=254)
    def __str__(self):
        return self.nom
    


class Commande(models.Model):
    designation = models.CharField(max_length=50 ,null=True)
    nombreSachet = models.IntegerField(null=True)
    poids =models.FloatField
    prix=models.FloatField 
    date_commande = models.DateField(default=timezone.now)
    client_commande = models.ForeignKey(Client, on_delete=models.CASCADE ,null=True)
    
    def __str__(self):
        return self.designantion

class Attribution(models.Model):
    designantion = models.CharField(max_length=50 ,null=True)
    commande_attribution = models.ForeignKey(Commande, on_delete=models.CASCADE , null=True )
    livreur = models.ForeignKey(Livreur, on_delete=models.CASCADE , null=True)
    date = models.DateField(default=timezone.now) 
    gestionnaire = models.ForeignKey(Gestionnaire, on_delete= models.CASCADE ,null=True)
    commentaire = models.TextField(max_length=300,null=True)

    def __str__(self):
        return self.designantion

class Livraison(models.Model):
    designation = models.CharField(max_length= 50 ,null=True) 
    commande_livraison = models.ForeignKey(Commande, on_delete=models.CASCADE ,null=True)
    #client_livraison = models.ForeignKey(Client, on_delete=models.CASCADE) 
    livreur_livraison = models.ForeignKey(Livreur, on_delete=models.CASCADE ,null=True)
    etat = models.BooleanField(null=True) # true pour livré false pour pas encore livré

    def __str__(self):
        return self.designation