from gbapi.viewsets import ClientViewset 
from rest_framework import routers

from gbapi.viewsets import LivreurViewset 
from gbapi.viewsets import GestionnaireViewset 
from gbapi.viewsets import CommandeViewset
from gbapi.viewsets import AttributionViewset
from gbapi.viewsets import LivraisonViewset

from gbapi.viewsets import UserViewset

router = routers.DefaultRouter()
router.register('client',ClientViewset)
router.register('livreur',LivreurViewset)
router.register('gestionnaire',GestionnaireViewset)
router.register('commande',CommandeViewset)
router.register('livraison',LivraisonViewset)
router.register('attribution',AttributionViewset)
router.register('user',UserViewset)