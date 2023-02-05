from django.contrib import admin

# Register your models here. 
from .models import Client
from .models import Gestionnaire
from .models import Livreur
from .models import Livraison
from .models import Commande
from .models import Attribution

admin.site.register(Client) 
admin.site.register(Gestionnaire) 
admin.site.register(Livreur)
admin.site.register(Livraison) 
admin.site.register(Commande) 
admin.site.register(Attribution) 