from gbapi.viewsets import ClientViewset 
from rest_framework import routers

router = routers.DefaultRouter()
router.register('client',ClientViewset)