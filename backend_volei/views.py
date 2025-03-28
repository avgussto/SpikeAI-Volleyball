from django.shortcuts import render, redirect
from .forms import RegisterForm

def registro(request):
    return render(request, 'registro.html')

def inicio(request):
    return render(request, 'inicio.html')

def login(request):
    return render(request, 'login.html')
