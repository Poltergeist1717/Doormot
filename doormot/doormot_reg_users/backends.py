import logging
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist
from .models import Doormot_User_Individual_Owner, Doormot_User_Private_Organization_Owner, Doormot_User_Individual_Buyer, Doormot_User_Private_Organization_Buyer, Doormot_User_Individual_Tenant, Doormot_User_Private_Organization_Tenant, Doormot_User_Official_Agent, Doormot_User_Independent_Agent 

logger = logging.getLogger(__name__)

class DoormotCustomUserBackend(ModelBackend):

    def authenticate(self, request, user_type=None, username=None, email=None, password=None, **kwargs):

        if user_type == "Individual_owner":
            try:
                user = Doormot_User_Individual_Owner.objects.get(username=username) if username else Doormot_User_Individual_Owner.objects.get(email=email)
                if user.check_password(password):
                    return user
                return None
            except ObjectDoesNotExist as e:
                logger.exception('There was an error: %s', e)
                return None
                
           

        elif user_type == "Private_org_owner":
            try:
                user = Doormot_User_Private_Organization_Owner.objects.get(username=username) if username else Doormot_User_Private_Organization_Owner.objects.get(email=email)
                if user and user.check_password(password):
                    return user
                return None
            except ObjectDoesNotExist as e:
                logger.exception('There was an error: %s', e)
                return None
            

        
        elif user_type == "Individual_buyer":
            try:
                user = Doormot_User_Individual_Buyer.objects.get(username=username) if username else Doormot_User_Individual_Buyer.objects.get(email=email)
                if user and user.check_password(password):
                    return user
                return None
            except ObjectDoesNotExist as e:
                logger.exception('There was an error: %s', e)
                return None
            

        elif user_type == "Private_org_buyer":
            try:
                user = Doormot_User_Private_Organization_Buyer.objects.get(username=username) if username else Doormot_User_Private_Organization_Buyer.objects.get(email=email)
                if user and user.check_password(password):
                    return user
                return None
            except ObjectDoesNotExist as e:
                logger.exception('There was an error: %s', e)
                return None
            

        
        elif user_type == "Individual_tenant":
            try:
                user = Doormot_User_Individual_Tenant.objects.get(username=username) if username else Doormot_User_Individual_Tenant.objects.get(email=email)
                if user and user.check_password(password):
                    return user
                return None
            except ObjectDoesNotExist as e:
                logger.exception('There was an error: %s', e)
                return None
            

        elif user_type == "Private_org_tenant":
            try:
                user = Doormot_User_Private_Organization_Tenant.objects.get(username=username) if username else Doormot_User_Private_Organization_Tenant.objects.get(email=email)
                if user and user.check_password(password):
                    return user
                return None
            except ObjectDoesNotExist as e:
                logger.exception('There was an error: %s', e)
                return None
            
            


        elif user_type == "Official_agent":
            try:
                user = Doormot_User_Official_Agent.objects.get(username=username) if username else Doormot_User_Official_Agent.objects.get(email=email)
                if user and user.check_password(password):
                    return user
                return None
            except ObjectDoesNotExist as e:
                logger.exception('There was an error: %s', e)
                return None
            

        elif user_type == "Independent_agent":
            try:
                user = Doormot_User_Independent_Agent.objects.get(username=username) if username else Doormot_User_Independent_Agent.objects.get(email=email)
                if user and user.check_password(password):
                    return user
                return None
            except ObjectDoesNotExist as e:
                logger.exception('There was an error: %s', e)
                return None
