from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('download/<int:pk>/', views.download_paper, name='download_paper'),
    path('pastpapers/', views.papers, name='papers'),
]
