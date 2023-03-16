from rest_framework import viewsets
from dashbord import models
from . import serializers 
from rest_framework import permissions 

from django.contrib.auth.models import User, Group

from django.utils.decorators import method_decorator
#from django.utils.decorators import *
from django.views.decorators.csrf import csrf_exempt

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


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
    
@method_decorator(csrf_exempt,'dispatch')
class CustomAuthToken(ObtainAuthToken):
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            # 'email': user.email
        })


#'csrfmiddlewaretoken': ['kU3GMFCdu2CY4QdGPPbnEEOXXvfJKyrVGIeiKAqJuMN3FN84hIFO2M3ML2VQ77uD']    