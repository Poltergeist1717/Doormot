from .forms import (
    Individual_owner_registeration_form,
    Individual_Owner_Login_Form,
    Private_Organizations_Owner_Registeration_Form, 
    Private_Organizations_Owner_Login_Form, 
    Individual_buyer_registeration_form, 
    Individual_Buyer_Login_Form, 
    Private_Organizations_Buyer_Registeration_Form, 
    Private_Organizations_Buyer_Login_Form, 
    Individual_Tenant_Registration_Form, 
    Individual_Tenant_Login_Form, 
    Private_Organization_Tenant_Registration_Form, 
    Private_Organization_Tenant_Login_Form, 
    Official_Agent_Registration_Form, 
    Official_Agent_Login_Form, 
    Doormot_User_Independent_Agent_Registration_Form, 
    Doormot_User_Independent_Agent_Login_Form

)





def retrun_form_type(user_type):
    if user_type == 'Individual_owner':
        return Individual_Owner_Login_Form()
    if user_type == 'Private_org_owner':
        return Private_Organizations_Owner_Login_Form()

        
    if user_type == 'Individual_buyer':
        return Individual_Buyer_Login_Form()        
    if user_type == 'Private_org_buyer':
        return Private_Organizations_Buyer_Login_Form()
        
    if user_type == 'Individual_tenant':
       return Individual_Tenant_Login_Form()
    if user_type == 'Private_org_tenant':
       return Private_Organization_Tenant_Login_Form()

    if user_type == 'Official_agent':
        return Official_Agent_Login_Form()
    if user_type == 'Independent_agent':
        return Doormot_User_Independent_Agent_Login_Form()