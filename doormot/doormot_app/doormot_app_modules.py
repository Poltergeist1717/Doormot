# CAUTION! CAUTION!! CAUTION!!!
# CAUTION: Do not make any changes here except it is absolutely necessary and throughly thought through
# This codes are highly delecate, a little bend can make them break - so, deal with care

from doormot_reg_users.models import (
    Doormot_User_Individual_Owner, 
    Doormot_User_Private_Organization_Owner, 
    Doormot_User_Individual_Buyer, 
    Doormot_User_Private_Organization_Buyer, 
    Doormot_User_Individual_Tenant, 
    Doormot_User_Private_Organization_Tenant, 
    Doormot_User_Official_Agent, 
    Doormot_User_Independent_Agent 
)

# Type: Function
# Task: Returns user object
def return_user_object(user_pk, user_type):
    user_type = user_type
    user_pk = user_pk
    if user_pk:
        if user_type == 'Individual_owner':
            user = Doormot_User_Individual_Owner.objects.get(pk=user_pk)
            return user
        if user_type == 'Private_org_owner':
            user = Doormot_User_Private_Organization_Owner.objects.get(pk=user_pk)
            return user

        if user_type == 'Individual_buyer':
            user = Doormot_User_Individual_Buyer.objects.get(pk=user_pk)
            return user    
        if user_type == 'Private_org_buyer':
            user = Doormot_User_Private_Organization_Buyer.objects.get(pk=user_pk)

        if user_type == 'Individual_tenant':
            user = Doormot_User_Individual_Tenant.objects.get(pk=user_pk)
            return user
        if user_type == 'Private_org_tenant':
            user = Doormot_User_Private_Organization_Tenant.objects.get(pk=user_pk)
            return user

        if user_type == 'Official_agent':
            user = Doormot_User_Official_Agent.objects.get(pk=user_pk)
            return user
        if user_type == 'Independent_agent':
            user = Doormot_User_Independent_Agent.objects.get(pk=user_pk)
            return user


# class user_object(user_type, user_pk, *args, **kwargs):
    
#     def return_user_object(slef, user_pk, user_type):
#         self.user_type = user_type
#         self.user_pk = user_pk
#         if self.user_pk:
#             if self.user_type == 'Individual_owner':
#                 user = Doormot_User_Individual_Owner.objects.get(pk=self.user_pk)
#                 return user
#             if self.user_type == 'Private_org_owner':
#                 user = Doormot_User_Private_Organization_Owner.objects.get(pk=self.user_pk)
#                 return user

#             if self.user_type == 'Individual_buyer':
#                 user = Doormot_User_Individual_Buyer.objects.get(pk=self.user_pk)
#                 return user    
#             if self.user_type == 'Private_org_buyer':
#                 user = Doormot_User_Private_Organization_Buyer.objects.get(pk=self.user_pk)

#             if self.user_type == 'Individual_tenant':
#                 user = Doormot_User_Individual_Tenant.objects.get(pk=self.user_pk)
#                 return user
#             if self.user_type == 'Private_org_tenant':
#                 user = Doormot_User_Private_Organization_Tenant.objects.get(pk=self.user_pk)
#                 return user

#             if self.user_type == 'Official_agent':
#                 user = Doormot_User_Official_Agent.objects.get(pk=self.user_pk)
#                 return user
#             if self.user_type == 'Independent_agent':
#                 user = Doormot_User_Independent_Agent.objects.get(pk=self.user_pk)
#                 return user

#     def return_single_user_object(self):
#         if user_type == user_type:
