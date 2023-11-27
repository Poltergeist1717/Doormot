from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.views import LoginView
from django.views import View
from .backends import DoormotCustomUserBackend
from .doormot_reg_module2 import retrun_form_type
# from .forms import (
#     Individual_owner_registeration_form,
#     Individual_Owner_Login_Form,
#     Private_Organizations_Owner_Registeration_Form, 
#     Private_Organizations_Owner_Login_Form, 
#     Individual_buyer_registeration_form, 
#     Individual_Buyer_Login_Form, 
#     Private_Organizations_Buyer_Registeration_Form, 
#     Private_Organizations_Buyer_Login_Form, 
#     Individual_Tenant_Registration_Form, 
#     Individual_Tenant_Login_Form, 
#     Private_Organization_Tenant_Registration_Form, 
#     Private_Organization_Tenant_Login_Form, 
#     Official_Agent_Registration_Form, 
#     Official_Agent_Login_Form, 
#     Doormot_User_Independent_Agent_Registration_Form, 
#     Doormot_User_Independent_Agent_Login_Form

# )

class DoormotCustomLoginView(LoginView):
    def get(self, request):
        name = None
        user_type = request.GET.get('user_type')

        request.session['user_type'] = user_type
        name = user_type

        form = retrun_form_type(user_type)

        return render(
            request, 'doormot_reg_users/login.html', 
            {"title":"Login", 'form':form, 'name':name, 'user_type':user_type}
        )

    def post(self, request):
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_type = request.session.get('user_type')

        # Failed login count identifier set to username and user_type
        false_log_identifier = f"{user_type}_{username}" 
        # Tries to retrieve Failed login count against identifier
        # If none exists, sets default count to 5
        false_log_count = request.session.get(f'false_log_count_{false_log_identifier}', 5)

        name = user_type
        form = retrun_form_type(user_type)


        false_log = 0


        # Authenticate user based on the provided credentials
        user = DoormotCustomUserBackend.authenticate(self, request=request, username=username, email=email, password=password, user_type=user_type, backend = 'doormot.doormot_reg_users.backends.DoormotCustomUserBackend')

        if user is not None:
            if user.is_active:
                # Please do not tamper
                user.backend = 'doormot.doormot_reg_users.backends.DoormotCustomUserBackend' # informs django which backend authentication to use
                login(request, user)
                request.session['user'] = user.pk
                request.session.get(f'false_log_count_{false_log_identifier}', 5) # Reset False Login Count to default after user logs in
                return render (request, 'doormot_app/home.html', {"title":"Home", "user":user})
            else:
                return render (
                    request, 'doormot_reg_users/account_disabled.html', {"title":"Account Disabled", "user":user})   
        else:
            false_log_count -= 1
            request.session[f'false_log_count_{false_log_identifier}'] = false_log_count

            if false_log_count > 0:
                message = f"Error: Login failed! You have only {false_log_count} attempts left!"
                return render(request, 'doormot_reg_users/login.html', {"title":"Login", 'form':form, 'name':name, 'user_type':user_type, 'message':message, 'false_log_count':false_log_count},)
            else:
                return render (request, 'doormot_reg_users/account_disabled.html', {"title":"Account Disabled", "user":user}) 
                        


class DoormotCustomLogoutView(View):
    def get(self, request): 
        logout(request) # Call the django built-in logout function to log out the current user
       
        return redirect('doormot-home')



def register(request):
    return render(request, 'doormot_reg_users/register.html', {'title':'Register'})










# SECTION: OWNERS
# Owners Views: Individual, Private Organization and Government

# Individual Owner Registeration View
def individual_owner(request):
    Individual_owner_registeration_form()

    if request.method == 'POST':
        form = Individual_owner_registeration_form(request.POST)
        if form.is_valid():
            profile = form.save()
            # profile.user = request.user
            # profile.save()
            return redirect('doormot-reg-users-login')
    else:
        form = Individual_owner_registeration_form()
    return render(request, 'doormot_reg_users/individual_owner.html', {'title':'Individual-Owner-Registration', 'form': form})


# Private Organization Owner Registeration View
def private_organization_owner(request):
    form = Private_Organizations_Owner_Registeration_Form()

    if request.method == 'POST':
        form = Private_Organizations_Owner_Registeration_Form(request.POST)
        
        if form.is_valid():
            profile = form.save()
            return redirect('doormot-reg-users-login')
        else:
            form = Private_Organizations_Owner_Registeration_Form()
    return render(request, 'doormot_reg_users/private_organization_owner.html', {'title':'Private-Organization-Owner-Registration', 'form': form})




















# SECTION: TENANTS
# Tenants views: Individual, Private Organization and Government


def individual_tenant(request):
    form = Individual_Tenant_Registration_Form()

    if request.method == 'POST':
        form = Individual_Tenant_Registration_Form(request.POST)
        
        if form.is_valid():
            profile = form.save()
            return redirect('doormot-reg-users-login')
        else:
            form = Individual_Tenant_Registration_Form()
    return render(request, 'doormot_reg_users/tenant.html', {'title':'Individual-Tenant-registration', 'form': form})


def private_organization_tenant(request):
    form = Private_Organization_Tenant_Registration_Form()

    if request.method == 'POST':
        form = Private_Organization_Tenant_Registration_Form(request.POST)
        
        if form.is_valid():
            profile = form.save()
            return redirect('doormot-reg-users-login')
        else:
            form = Private_Organization_Tenant_Registration_Form()
    return render(request, 'doormot_reg_users/private_organization_tenant.html', {'title':'Private-Organization-Tenant-Registration', 'form': form})
















# SECTION: BUYERS
# Buyers Views: Individual, Private Organization and Government

# Individual Buyer Registeration View
def individual_buyer(request):
    form = Individual_buyer_registeration_form()

    if request.method == 'POST':
        form = Individual_buyer_registeration_form(request.POST)
        
        if form.is_valid():
            profile = form.save()
            return redirect('doormot-reg-users-login')
        else:
            form = Individual_buyer_registeration_form()
    return render(request, 'doormot_reg_users/buyer.html', {'title':'Individual-Buyer-Registration', 'form': form})

# Private Organization Buyer Registeration View
def private_organization_buyer(request):
    form = Private_Organizations_Buyer_Registeration_Form()

    if request.method == 'POST':
        form = Private_Organizations_Buyer_Registeration_Form(request.POST)
        
        if form.is_valid():
            profile = form.save()
            return redirect('doormot-reg-users-login')
        else:
            form = Private_Organizations_Buyer_Registeration_Form()
    return render(request, 'doormot_reg_users/private_organization_buyer.html', {'title':'Private-Organization-Buyer-Registration', 'form': form})





















# SECTION: AGENTS
# Agents Views: Individual, Private Organization and Government

# Official Agent Registeration View
def official_agent(request):
    form = Official_Agent_Registration_Form()

    if request.method == 'POST':
        form = Official_Agent_Registration_Form(request.POST)

        if form.is_valid():
            profile = form.save()
            return redirect('doormot-reg-users-login')
        else:
            form = Official_Agent_Registration_Form()
        
    return render(request, 'doormot_reg_users/official_agent.html', {'title':'Official-Agent-registration', 'form':form})



# Independent Agent Registeration View
def independent_agent(request):
    form = Doormot_User_Independent_Agent_Registration_Form()

    if request.method == 'POST':
        form = Doormot_User_Independent_Agent_Registration_Form(request.POST)

        if form.is_valid():
            profile = form.save()
            return redirect('doormot-reg-users-login')
        else:
            form = Doormot_User_Independent_Agent_Registration_Form()
            
    return render(request, 'doormot_reg_users/independent_agent.html', {'title':'Independent-Agent-registration', 'form':form})








# SECTION: OWNERS
# Owners models: Individual, Private Organization and Government

def partner(request):
    return render(request, 'doormot_reg_users/partner.html', {'title':'Partner-registration'})



# SECTION: OWNERS
# Owners models: Individual, Private Organization and Government

def logistics(request):
    return render(request, 'doormot_reg_users/logistics.html', {'title':'Logistics-registration'})



# SECTION: DISABLED ACCOUNTS
# Disabled accounts views: Individual, Private Organization and Government

def disabled_account(request):
    return render(request, 'doormot_reg_users/account_disabled.html', {'title':'Account_Disabled'})





# SECTION: LOGIN FAILED
# Login failed views: Individual, Private Organization and Government

def login_failed(request):
    return render(request, 'doormot_reg_users/login_failed.html', {'title':'Login_Failed'})