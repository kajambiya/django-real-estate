from django.urls import path

from .views import (ListAgentsPropertiesAPIView, ListAllPropertiesAPIView, create_property_api_view, update_property_api_view,
                    delete_property_api_view, PropertyDetailView, PropertySearchAPIView)


urlpatterns = [
    path('all/', ListAllPropertiesAPIView.as_view(), name='all-properties'),
    path('agents/', ListAgentsPropertiesAPIView.as_view(), name='agents-properties'),
    path('create/', create_property_api_view, name='property-create'),
    path('details/<slug:slug>/', PropertyDetailView.as_view(), name='property-details'),
    path('update/<slug:slug>/', update_property_api_view, name='property-update'),
    path('delete/<slug:slug>/', delete_property_api_view, name='delete-property'),
    path('search/', PropertySearchAPIView.as_view(), name='search-property'),
]