from django.urls import path
from . import views
from .views import profile_views, property_uploader_profile_view


urlpatterns = [
        path('current_user=<str:username>/', profile_views.as_view(), name='doormot_users_profiles_profile_views'),
        path('property_uploader_profile=<str:username>/', property_uploader_profile_view.as_view(), name='doormot_users_profiles_property_uploader_profile_views'),
    ]