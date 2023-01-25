from rest_framework import viewsets
from dashbord import models
from . import serializers

class ClientViewset(viewsets.ModelViewSet):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer