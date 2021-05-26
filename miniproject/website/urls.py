from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='website-home'), 
    path('about/', views.about, name='website-about'), 
    path('biological/', views.biological, name='website-biological'),
    path('chemical/', views.chemical, name='website-chemical'), 
    path('cyclone/', views.cyclone, name='website-cyclone'),
    path('earthquake/', views.earthquake, name='website-earthquake'),
    path('floods/', views.floods, name='website-floods'),  
    path('heatwave/', views.heatwave, name='website-heatwave'),
    path('nuclear/', views.nuclear, name='website-nuclear'), 
    path('tsunami/', views.tsunami, name='website-tsunami'),
    path('urbanfloods/', views.urbanfloods, name='website-urbanfloods'),
    path('satellite/', views.satellite, name='website-satellite'),
]