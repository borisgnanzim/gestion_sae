from django.contrib import admin
from django.urls import path, include
from dashbord import views
#from .router import router

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('dashbord/', views.dashbord),
    # path('', views.Login),
    # path('api/',include(router.urls)) 
    
    # path("enregistrer_client/", views.enregistrer_client, name="enregistrer_client")

    # Ajout du 14-03-2023 11H23

    path('dashboard/', views.dashboard,name="dashboard"),
    path('enregistrer_client/', views.enregistrer_client,name="enregistrer_client"),
    path('liste_client/', views.liste_client,name="liste_client"),
    path('enregistrer_commande/', views.enregistrer_commande,name="enregistrer_commande"),
    path('liste_commande/', views.liste_commande,name="liste_commande"),
    path('statistique_general/', views.statistique,name="statistique_general",),
    path('statistique/<int:pk>', views.statistique,name="statistique",),
    path('recapitulatif/', views.recapitulatif,name="recapitulatif"),
    path('imprimer/', views.imprimer,name="imprimer"),
    path('modifier_client/<int:pk>', views.modifier_client,name="modifier_client"),
    path('modifier_commande/<int:pk>', views.modifier_commande,name="modifier_commande"),
    path('modifier_livraison/<int:pk>', views.modifier_livraison,name="modifier_livraison"),
    path('gestion_livraison_manuelle/', views.gestion_livraison_manuelle,name="gestion_livraison_manuelle"),
    path('gestion_livraison_automatique/', views.gestion_livraison_automatique,name="gestion_livraison_automatique"),
    path('liste_livraison/', views.liste_livraison,name="liste_livraison"),
    path('enregistrer_livreur/', views.enregistrer_livreur,name="enregistrer_livreur"),
    path('liste_livreur/', views.liste_livreur,name="liste_livreur"),
    

]