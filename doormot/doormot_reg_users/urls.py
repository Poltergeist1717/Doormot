from django.urls import path
from . import views
from .views import DoormotCustomLoginView, DoormotCustomLogoutView

urlpatterns = [
            path('', views.register, name='doormot-reg-users-register'),

            path('individual_owner/', views.individual_owner, name='doormot-reg-users-individual-owner'),
            path('private_organization_owner/', views.private_organization_owner, name='doormot-reg-users-private-organization-owner'),

            path('individual_buyer/', views.individual_buyer, name='doormot-reg-users-individual-buyer'),
            path('private_organization_buyer/', views.private_organization_buyer, name='doormot-reg-users-private-organization-buyer'),
            
            path('individual_tenant/', views.individual_tenant, name='doormot-reg-users-individual-tenant'),
            path('private_organization_tenant/', views.private_organization_tenant, name='doormot-reg-users-private-organization-tenant'),

            path('official_agent/', views.official_agent, name='doormot-reg-users-official-agent'),
            path('independent_agent/', views.independent_agent, name='doormot-reg-users-independent-agent'),

            path('logistics/', views.logistics, name='doormot-reg-users-logistics'),
            path('partner/', views.partner, name='doormot-reg-users-partner'),

            path('login/', DoormotCustomLoginView.as_view(), name='doormot-reg-users-login'),
            path('account_disabled/', views.disabled_account, name='doormot-reg-users-account-disabled'),
            path('login_failed/', views.login_failed, name='doormot-reg-users-login-failed'),
            path('logout/', DoormotCustomLogoutView.as_view(), name='doormot_custom_logout'),
        ]
