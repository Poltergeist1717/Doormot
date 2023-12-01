from .forms import (
    Individual_Owner_Login_Form, 
    Private_Organizations_Owner_Login_Form, 
    Individual_Buyer_Login_Form,  
    Private_Organizations_Buyer_Login_Form, 
    Individual_Tenant_Login_Form, 
    Private_Organization_Tenant_Login_Form, 
    Official_Agent_Login_Form, 
    Doormot_User_Independent_Agent_Login_Form

)





def return_form_type(user_type):
   
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



def return_form_title(user_type):
    title_mapping = {
            'Individual_owner': 'Individual Owner Profile',
            'Private_org_owner': 'Private Org Owner Profile',
            'Individual_buyer': 'Individual Buyer Profile',
            'Private_org_buyer': 'Private Org Buyer Profile',
            'Individual_tenant': 'Individual Tenant Profile',
            'Private_org_tenant': 'Private Org Tenant Profile',
            'Independent_agent': 'Independent Agent Profile',
            'Official_agent': 'Official Agent Profile',
        }
    title = title_mapping.get(user_type, 'Individual Owner Profile')
    return title
