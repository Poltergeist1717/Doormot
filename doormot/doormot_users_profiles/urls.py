from django.urls import path
from . import views

urlpatterns = [
        path('individual_owner_profile/', views.individual_owner_profile_view, name='doormot_users_profiles_individual_owner_profile'),
    ]