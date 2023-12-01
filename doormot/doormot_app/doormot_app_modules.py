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
# Task: Returns user object by user_type and user_pk
def return_user_object(user_pk, user_type):
    user_type = user_type
    user_pk = user_pk
    user_type_map = {
        'Individual_owner': Doormot_User_Individual_Owner,
        'Private_org_owner': Doormot_User_Private_Organization_Owner,
        'Individual_buyer': Doormot_User_Individual_Buyer,
        'Private_org_buyer': Doormot_User_Private_Organization_Buyer,
        'Individual_tenant': Doormot_User_Individual_Tenant,
        'Private_org_tenant': Doormot_User_Private_Organization_Tenant,
        'Official_agent': Doormot_User_Official_Agent,
        'Independent_agent': Doormot_User_Independent_Agent,
    }

    if user_pk:
        if user_type in user_type_map:
            model_class = user_type_map[user_type]
            user = model_class.objects.get(pk=user_pk)
            return user
        else:
            raise ValueError("Invalid user_type")
            return None




# Type: Class
# Task: Returns user object, sets models fields value and returns models fields value
class Return_Model_Object_Fields_Handler:
    # Define a mapping of user types to model classes
    user_type_map = {
        'Individual_owner': Doormot_User_Individual_Owner,
        'Private_org_owner': Doormot_User_Private_Organization_Owner,
        'Individual_buyer': Doormot_User_Individual_Buyer,
        'Private_org_buyer': Doormot_User_Private_Organization_Buyer,
        'Individual_tenant': Doormot_User_Individual_Tenant,
        'Private_org_tenant': Doormot_User_Private_Organization_Tenant,
        'Official_agent': Doormot_User_Official_Agent,
        'Independent_agent': Doormot_User_Independent_Agent,
    }


    def __init__(self, username, user_type, *args, **kwargs):
        self.user_type = user_type
        self.username = username
        self.model_kwargs = kwargs

    def get_field_value(self, field_name, **kwargs):
        self.field_name = field_name
        if kwargs:
            # If additional kwargs are provided, use them
            model_kwargs = kwargs
        else:
            # Otherwise, use the kwargs from the class instantiation
            model_kwargs = self.model_kwargs

        if self.user_type in self.user_type_map:
            model_class = self.user_type_map[self.user_type]
            if model_class.objects.filter(**model_kwargs).exists():
                field_value = model_class.objects.filter(**model_kwargs).values(self.field_name).get()[self.field_name]
                return field_value
            else:
                return None
        else:
            raise ValueError("Invalid user_type")
            return None

    def return_user_object(self, **kwargs):
        if kwargs:
            # If additional kwargs are provided, use them
            model_kwargs = kwargs
        else:
            # Otherwise, use the kwargs from the class instantiation
            model_kwargs = self.model_kwargs

        if self.user_type in self.user_type_map:
            model_class = self.user_type_map[self.user_type]
            if model_class.objects.filter(**model_kwargs).exists():
                user = model_class.objects.get(**model_kwargs)
                return user
            else:
                return None
        else:
            raise ValueError("Invalid user_type")
            return None

    def set_field_value(self, field_name, desired_value):
        self.field_name = field_name
        user_object = self.return_user_object()
        if user_object is not None:
            user_object.__setattr__(self.field_name, desired_value)
            user_object.save()
        else:
            pass
