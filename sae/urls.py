"""sae URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import viewsdlzdlz
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from dashbord import views

from .router import router

from rest_framework import authtoken
from django.urls import path, include

from gbapi.viewsets import CustomAuthToken

from rest_framework.authtoken import views as vw


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashbord/', views.dashbord),
    path('dashboard/', views.dashboard),
    path('', views.Login),
    path('#', views.dashbord),
    path('login/',views.Login),
    path('logout/',views.Logout),
    path('api/',include(router.urls)) ,

    path('api-token-auth/', authtoken.views.obtain_auth_token),
    path('api-token-auth/', CustomAuthToken.as_view()) ,
    
    path('api/auth', include('rest_framework.urls', namespace='rest_framework')),
    path('api/auth/token', vw.obtain_auth_token)  , 

    #path('enregistrer_client/', views.enregistrer_client, name="enregistrer_client"),

# Ajout du 14-03-2023 11h19
    path('gestion/', include('dashbord.urls')),

    
]



