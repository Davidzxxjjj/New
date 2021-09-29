from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    return render(request, 'index.html')

def mascota(request):
    allmascota = Mascota.objects.all()
    return render(request, 'mascota.html',{'allmascota':allmascota})

def dueños(request):
    alldueños = Cliente.objects.all()
    return render(request, 'dueños.html',{'alldueños':alldueños})

def citas(request):
    allcitas = Cita.objects.all()
    return render(request, 'citas.html',{'allcitas':allcitas})
