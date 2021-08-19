from django.urls import path, include
from . import views

urlpatterns = [
    path('connexion', views.login_admin, name='login_admin'),
    path('', views.dashboard_jury, name='dashboard_jury'),
    path('<int:jury_id>', views.jury_info, name='jury_info'),
    path('inscription', views.register_admin, name='register_admin'),
    path('deconnection', views.logout_admin, name='logout_admin'),
    # path('tableau', views.dashboard, name='dashboard'),
]
