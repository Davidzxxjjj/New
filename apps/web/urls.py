from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index.html'),
    path('about/', about, name='about.html'),
    path('blog/', blog, name='blog.html'),
    path('blogsingle', blogsingle, name='blog-single.html'),
    path('contact', contact, name='contact.html'),
    path('gallery', gallery, name='gallery.html'),
    path('main', main, name='main.html'),
    path('pricing', pricin, name='pricing.html'),
    path('services', services, name='services.html'),
    path('vet', vet, name='vet.html'),
]