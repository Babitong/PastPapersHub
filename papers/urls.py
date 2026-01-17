from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('download/<int:pk>/', views.download_paper, name='download_paper'),
    path('pastpapers/', views.PastPaperListView.as_view(), name='papers'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
]
