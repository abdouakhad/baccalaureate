from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:student_id>', views.student_info, name='student_info'),
    path('a-propos/', views.about, name='about'),
]
