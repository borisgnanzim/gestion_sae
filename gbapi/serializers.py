from rest_framework import serializers 
from dashbord.models import * 

class ClientSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Client
        fields = "__all__"
     