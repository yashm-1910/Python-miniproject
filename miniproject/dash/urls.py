from . import views
from django.urls import path

urlpatterns = [
    path('cases/', views.cases, name = "dash-cases"),
    path('vaccine/', views.vaccine, name = "dash-vaccine"),
]