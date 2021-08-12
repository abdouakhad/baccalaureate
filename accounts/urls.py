from django.urls import path, include
from . import views

urlpatterns = [
    path('connexion', views.login, name='login'),
    path('inscription', views.register, name='register'),
    path('deconnection', views.logout, name='logout'),
    path('tableau', views.dashboard, name='dashboard'),
]
