from rest_framework import viewsets
from dashbord import models
from . import serializers 
from rest_framework import permissions 

from django.contrib.auth.models import User, Group


class ClientViewset(viewsets.ModelViewSet):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
    permission_classes = [permissions.IsAuthenticated] 
    
class LivreurViewset(viewsets.ModelViewSet):
    queryset = models.Livreur.objects.all()
    serializer_class = serializers.LivreurSerializer
    permission_classes = [permissions.IsAuthenticated] 
    
class GestionnaireViewset(viewsets.ModelViewSet):
    queryset = models.Gestionnaire.objects.all()
    serializer_class = serializers.GestionnaireSerializer
    permission_classes = [permissions.IsAuthenticated] 

class CommandeViewset(viewsets.ModelViewSet):
    queryset = models.Commande.objects.all()
    serializer_class = serializers.CommandeSerializer
    permission_classes = [permissions.IsAuthenticated] 
    
class AttributionViewset(viewsets.ModelViewSet):
    queryset = models.Attribution.objects.all()
    serializer_class = serializers.AttributionSerializer
    permission_classes = [permissions.IsAuthenticated] 
    
class LivraisonViewset(viewsets.ModelViewSet):
    queryset = models.Livraison.objects.all()
    serializer_class = serializers.LivraisonSerializer
    permission_classes = [permissions.IsAuthenticated]  

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]    
    