from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse
from django.http import Http404
from django.shortcuts import get_object_or_404
import logging
from doormot_app.doormot_app_modules import return_user_object
from doormot_reg_users.models import (
    Doormot_User_Individual_Owner, 
    Doormot_User_Private_Organization_Owner,
    Doormot_User_Official_Agent, 
    Doormot_User_Independent_Agent 
)


logger = logging.getLogger(__name__)


class profile_views(View, LoginRequiredMixin):

    def get(self, request, *args, **kwargs):
        user_type = request.session.get('user_type')
        user_pk = request.session.get('user')
        username = self.request.user.username

        user = return_user_object(user_pk, user_type)

        try:
            if user:
                template_mapping = {
                        'Individual_owner': 'doormot_users_profiles/individuals_profile.html',
                        'Private_org_owner': 'doormot_users_profiles/orgs_profile.html',
                        'Individual_buyer': 'doormot_users_profiles/individuals_profile.html',
                        'Private_org_buyer': 'doormot_users_profiles/orgs_profile.html',
                        'Individual_tenant': 'doormot_users_profiles/individuals_profile.html',
                        'Private_org_tenant': 'doormot_users_profiles/orgs_profile.html',
                        'Independent_agent': 'doormot_users_profiles/official_agent_profile.html',
                        'Official_agent': 'doormot_users_profiles/official_agent_profile.html',
                    }
                    
                template_name = template_mapping.get(user_type, 'doormot_users_profiles/individual_owner_profile.html')

                profile_title_mapping = {
                        'Individual_owner': 'Individual Owner Proifle',
                        'Private_org_owner': 'Private Org Owner Profile',
                        'Individual_buyer': 'Individual Buyer Profile',
                        'Private_org_buyer': 'Private Org Buyer Profile',
                        'Individual_tenant': 'Individual Tenant Proifle',
                        'Private_org_tenant': 'Private Org Tenant Profile',
                        'Independent_agent': 'Independent Agent Profile',
                        'Official_agent': 'Official Agent Profile',
                    }

                profile_title = profile_title_mapping.get(user_type, 'Individual Owner Proifle')

                return render(request, template_name, {"title":profile_title, "user":user, "username":username})

        except Exception as e:
            logger.exception("There was an error: %s", e)


        #return render(request, 'some_error_template.html', {"error_message": "An error occurred"})


class property_uploader_profile_view(View):

    def get(self, request, *args, **kwargs):
        username_query = self.request.GET.get('username')
        user_type = self.request.GET.get('user_type')
    
        try:
            user_models_mapping = {
                'Individual_owner':Doormot_User_Individual_Owner, 
                'Private_org_owner':Doormot_User_Private_Organization_Owner, 
                'Official_agent':Doormot_User_Official_Agent, 
                'Independent_agent':Doormot_User_Independent_Agent,
            }
            user_model = user_models_mapping.get(user_type, Doormot_User_Individual_Owner)

            user = get_object_or_404(user_model, username=username_query)

            if user:
                template_mapping = {
                    'Individual_owner': 'doormot_users_profiles/individuals_profile.html',
                    'Private_org_owner': 'doormot_users_profiles/orgs_profile.html',
                    'Independent_agent': 'doormot_users_profiles/view_agent_profile_base_temp.html',
                    'Official_agent': 'doormot_users_profiles/official_agent_profile.html',
                    }
                        
                template_name = template_mapping.get(user_type)

                profile_title_mapping = {
                    'Individual_owner': 'Individual Owner Proifle',
                    'Private_org_owner': 'Private Org Owner Profile',
                    'Independent_agent': 'Independent Agent Profile',
                    'Official_agent': 'Official Agent Profile',
                        }

                profile_title = profile_title_mapping.get(user_type)

                return render(request, template_name, {"title":profile_title, "user":user, "username":username_query})

        except Exception as e:
            logger.exception("There was an error: %s", e)
