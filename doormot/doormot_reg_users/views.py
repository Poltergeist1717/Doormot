from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.views import View
from .forms import Individual_owner_registeration_form, Individual_Owner_Login_Form, Private_Organizations_Owner_Registeration_Form, Private_Organizations_Owner_Login_Form, Individual_buyer_registeration_form, Individual_Buyer_Login_Form, Private_Organizations_Buyer_Registeration_Form, Private_Organizations_Buyer_Login_Form, Individual_Tenant_Registration_Form, Individual_Tenant_Login_Form, Private_Organization_Tenant_Registration_Form, Private_Organization_Tenant_Login_Form, Official_Agent_Registration_Form, Official_Agent_Login_Form, Doormot_User_Independent_Agent_Registration_Form, Doormot_User_Independent_Agent_Login_Form


class DoormotCustomLoginView(View):
    user_type = None
    def get(self, request):
        name = None
        user_type = request.GET.get('user_type', 'Individual_owner')

        request.session['user_type'] = user_type
        name = user_type
        
        # Determine user type and render the appropriate login form
        if user_type == 'Individual_owner':
            form = Individual_Owner_Login_Form()
        if user_type == 'Private_org_owner':
            form = Private_Organizations_Owner_Login_Form()

        
        if user_type == 'Individual_buyer':
            form = Individual_Buyer_Login_Form()        
        if user_type == 'Private_org_buyer':
            form = Private_Organizations_Buyer_Login_Form()
        
        if user_type == 'Individual_tenant':
            form = Individual_Tenant_Login_Form()
        if user_type == 'Private_org_tenant':
            form = Private_Organization_Tenant_Login_Form()

        if user_type == 'Official_agent':
            form = Official_Agent_Login_Form()
        if user_type == 'Independent_agent':
            form = Doormot_User_Independent_Agent_Login_Form()

        return render(request, 'doormot_reg_users/login.html', {'form':form, 'name':name})

    def post(self, request):
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_type = request.session.get('user_type')

        # Authenticate user based on the provided credentials
        user = authenticate(request, username=username, email=email, password=password, user_type=user_type)

        print(user)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('doormot-home') 
            else:
                return redirect('doormot-reg-users-account-disabled')
        else:
            return redirect('doormot-reg-users-login-failed')


# class DoormotCustomLogoutView(View):
#     def get(self, request):
#         # Call the logout function to log out the current user
#         logout(request)
#         # Redirect to a page after logout (you can customize this)
#         return redirect('doormot-home')






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
    form = Doormot_User_Independent_Agent_Form()

    if request.method == 'POST':
        form = Doormot_User_Independent_Agent_Form(request.POST)

        if form.is_valid():
            profile = form.save()
            return redirect('doormot-reg-users-login')
        else:
            form = Doormot_User_Independent_Agent_Form()
            
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