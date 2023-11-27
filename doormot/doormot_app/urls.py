from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='doormot-home'),
        path('about/', views.about, name='doormot-about'),
        path('team/', views.team, name='doormot-team'),
        path('contact/', views.contact, name='doormot-contact'),
    ]