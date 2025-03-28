"""
URL configuration for backend_volei project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path  # Certifique-se de que esta linha está presente
from .views import inicio, registro, login# Importando as views que criamos

urlpatterns = [
    path('', inicio, name='inicio'),  # Tela inicial
    path('registro/', registro, name='registro'),
    path('login/', login, name='login') # Tela de registro
]