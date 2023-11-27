from django.urls import path
from . import views
from .views import profile_views


urlpatterns = [
        path('cureent_user=<str:username>/', profile_views.as_view(), name='doormot_users_profiles_profile_views'),
    ]