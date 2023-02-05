from rest_framework import serializers 
from dashbord.models import * 

class ClientSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Client
        fields = "__all__"
     
class LivreurSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Livreur
        fields = "__all__"

class GestionnaireSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Gestionnaire
        fields = "__all__"

class AttributionSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Attribution
        fields = "__all__"     
        
class CommandeSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Commande
        fields = "__all__"

class LivraisonSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Livraison
        fields = "__all__"
        