from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('mascota', mascota, name='mascota'),
    path('dueños', dueños, name='dueños'),
    path('citas', citas, name='citas'),
]
