from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    allMascota = Mascota.objects.all()
    return render (request, 'index.html',{'allMascota':allMascota})

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def blogsingle(request):
    return render(request, 'blog-single.html')

def contact(request):
    return render(request, 'contact.html')

def gallery(request):
    return render(request, 'gallery.html')

def main(request):
    return render(request, 'main.html')

def pricin(request):
    return render(request, 'pricing.html')

def services(request):
    return render(request, 'services.html')

def vet(request):
    return render(request, 'vet.html')
















