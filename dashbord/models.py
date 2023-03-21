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
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
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
    poids =models.FloatField(max_length=12 ,null=True)
    prix=models.FloatField(max_length=12 ,null=True) 
    date = models.DateField(default=datetime.today())
    client = models.ForeignKey(Client, on_delete=models.CASCADE ,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.designation

class Attribution(models.Model):
    designation = models.CharField(max_length=50 ,null=True)
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE , null=True ,unique=True )
    livreur = models.ForeignKey(Livreur, on_delete=models.CASCADE , null=True)
    date = models.DateField(default=timezone.now) 
    gestionnaire = models.ForeignKey(Gestionnaire, on_delete= models.CASCADE ,null=True)
    commentaire = models.TextField(max_length=300,null=True)

    def __str__(self):
        return self.designation

class Livraison(models.Model):
    designation = models.CharField(max_length= 50 ,null=True) 
    commande_livraison = models.ForeignKey(Commande, on_delete=models.CASCADE ,null=True)
    #client_livraison = models.ForeignKey(Client, on_delete=models.CASCADE) 
    livreur_livraison = models.ForeignKey(Livreur, on_delete=models.CASCADE ,null=True)
    etat = models.BooleanField(null=True) # true pour livré false pour pas encore livré
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.designation