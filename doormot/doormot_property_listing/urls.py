from django.urls import path
from . import views
from .views import post_property, filtered_property_view, filter_property_by_username
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('listed_properties/', views.general_listing, name='doormot-property-listing-general-listing'),
        path('upload_property/', post_property.as_view(), name='doormot-property-listing-upload-property'),
        path('filter_property/', filtered_property_view.as_view(), name='doormot-property-filter-upload-property'),
        path('filter_property_by_username/', filter_property_by_username.as_view(), name='doormot-property-filter-property-by-username'),
        path('property_more_details/', views.property_more_details, name='doormot-property-more-details'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)