from django.urls import path
from . import views
from .views import post_property

urlpatterns = [
        path('listed_properties/', views.general_listing, name='doormot-property-listing-general-listing'),
        path('upload_property/', post_property.as_view(), name='doormot-property-listing-upload-property'),
    ]