import logging
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.views import LoginView
from django.views import View
from .backends import DoormotCustomUserBackend
from .doormot_reg_module2 import return_form_type, return_form_title
from doormot_app.doormot_app_modules import Return_Model_Object_Fields_Handler
from .forms import (
    Individual_owner_registeration_form,
    Private_Organizations_Owner_Registeration_Form, 
    Individual_buyer_registeration_form, 
    Private_Organizations_Buyer_Registeration_Form, 
    Individual_Tenant_Registration_Form, 
    Private_Organization_Tenant_Registration_Form, 
    Official_Agent_Registration_Form, 
    Doormot_User_Independent_Agent_Registration_Form, 
    )

logger = logging.getLogger(__name__)



# Type: Class
# Name: Doormot Custom Login View
# Methods: get, post, authenticate_user 
# Tasks: Handles user authentication
#        Handles login logic for all user models
#        Handles failed login attempts and prevents false log in
#        Prevents non-registered users from logging in
#        Redirects non-registered users to register page
#        Handles non_active user or disabled accounts
#        Resets False log count field to default
#        Prevents simultaneous use of one account in two different places (A single account cannot log in, in different browsers at the same)

class DoormotCustomLoginView(LoginView):
    def get(self, request):
        user_type = request.GET.get('user_type')
        request.session['user_type'] = user_type
        title = return_form_title(user_type)
        form = return_form_type(user_type)

        return render(request, 'doormot_reg_users/login.html', {"title": "Login", 'form': form, 'title': title, 'user_type': user_type})

    def post(self, request):
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_type = request.session.get('user_type')
        request.session['username'] = username

        log_count_field_name = 'false_log_count' # Name of model field from which number of allowed false login atttempts is recorded
        handler_instance = Return_Model_Object_Fields_Handler(username=username, user_type=user_type) # Creates the class instance that handles returning user object, setting field value and updating field value.
        false_log_count_field_value = handler_instance.get_field_value(field_name=log_count_field_name, username=username)
        user_object = handler_instance.return_user_object(username=username)

        currently_logged_field_name = 'currently_logged_in' # Name of model field from which currently logged in user is recorded
        currently_logged_in_value = handler_instance.get_field_value(field_name=currently_logged_field_name, username=username)

        try:
            form = return_form_type(user_type)
            title = return_form_title(user_type)
                
            if user_object is not None and false_log_count_field_value is None:
                handler_instance.set_field_value(field_name=log_count_field_name, desired_value=6)
                false_log_count_field_value = 6 # Variable to hold the default value for false log count field for false log count field update

            if currently_logged_in_value == True: # Check if user currently logged in and prevents the use of one account in two places.
                message = "This account is currently logged in. If It wasn't you, reach out to customer care immediately!"
                return render(request, 'doormot_reg_users/login.html', {"title": "Login", 'form': form, 'title': title, 'user_type': user_type, 'message':message})
           
            if user_object is not None and false_log_count_field_value > 0:
                try:
                    form = return_form_type(user_type)
                    title = return_form_title(user_type)
                    user = self.authenticate_user(request, username, email, password, user_type) # Calls the custom authentication method
                    if user is not None and false_log_count_field_value > 0:
                        if user.is_active:
                            user.backend = 'doormot.doormot_reg_users.backends.DoormotCustomUserBackend' # Points django the backend to use for authentication
                            login(request, user)
                            request.session['user'] = user.pk
                            handler_instance.set_field_value(field_name=log_count_field_name, desired_value=None) # Resets False log count field to default
                            handler_instance.set_field_value(field_name=currently_logged_field_name, desired_value=True) # Sets Currently logged in field to True. Prevents the same account to be logged in another place
                            return render(request, 'doormot_app/home.html', {"title": "Home", "user": user})
                        else:
                            return render(request, 'doormot_reg_users/account_disabled.html', {"title": "Account Disabled", "user": user})
                    elif user is None and false_log_count_field_value > 0:
                        false_log_count_field_value -= 1 # Decreament of false log count variable for false log count field update
                        handler_instance.set_field_value(field_name=log_count_field_name, desired_value=false_log_count_field_value) # Updates the false log count field to the new decreased value
                        message = f"Error: Login Failed! You have {false_log_count_field_value} attempts left!"
                        return render(request, 'doormot_reg_users/login.html', {"title": "Login", 'form': form, 'title': title, 'user_type': user_type, 'message':message})
                    else:
                        return render(request, 'doormot_reg_users/account_disabled.html', {"title": "Account Disabled", "user": user})
                except Exception as e:
                    logger.exception('There was an Error logging in: %s', e)
                    return render(request, 'doormot_reg_users/login.html', {"title": "Login", 'form': form, 'title': title, 'user_type': user_type})
            elif user_object is None and false_log_count_field_value is None:
                message = "You do not have an account with us."
                return render(request, 'doormot_reg_users/register.html', {'title': 'Register', 'message': message})
            else:
                message = "You do not have an account with us."
                return render(request, 'doormot_reg_users/register.html', {'title': 'Register', 'message': message})
        except Exception as e:
            logger.exception('There was an Error logging in: %s', e)
            message = f"Error!: {e}"
            return render(request, 'doormot_reg_users/login.html', {"title": "Login", 'form': form, 'title': title, 'user_type': user_type, 'message':message}) 
    # Type: Mehtod 
    # Tasks: To authenticate user
    #        Calls DoormotCustomUserBackend class (a custom backend authentication) for authentication
    #        Returns user object on successful authentication
    #        Returns None if authetication fails
    def authenticate_user(self, request, username, email, password, user_type):
        user =  DoormotCustomUserBackend.authenticate(self, request=request, username=username, email=email, password=password, user_type=user_type, backend='doormot.doormot_reg_users.backends.DoormotCustomUserBackend')
        return user



# Type: Class
# Name: Doormot Custom Logout View 
# Tasks: Handles all users logout process
#        Sets Currently logged in field to False. (Enables user to log in another time)
class DoormotCustomLogoutView(View):
    def get(self, request):
        username = request.session.get('username')
        user_type = request.session.get('user_type')
        currently_logged_field_name = 'currently_logged_in'
        handler_instance = Return_Model_Object_Fields_Handler(username=username, user_type=user_type) # Creates the class instance that handles returning user object, setting field value and updating field value.
        logout(request) # Call the django built-in logout function to log out the current user
        handler_instance.set_field_value(field_name=currently_logged_field_name, desired_value=False) # Sets Currently logged in field to False. (Enables user to log in another time)
       
        return redirect('doormot-home')



def register(request):
    return render(request, 'doormot_reg_users/register.html', {'title':'Register'})










# SECTION: OWNERS
# Owners Views: Individual, Private Organization and Government

# Individual Owner Registeration View
def individual_owner(request):
    form = Individual_owner_registeration_form(request.POST)

    if request.method == 'POST':
        form = Individual_owner_registeration_form(request.POST)
        if form.is_valid():
            profile = form.save()
            # profile.user = request.user
            # profile.save()
            return redirect('doormot-reg-users-login')
        else:
            form = Individual_owner_registeration_form(request.POST)
            errors = form.errors
            values = errors.values()
            message = "Error(s)!:"
            return render(request, 'doormot_reg_users/individual_owner.html', {'title':'Individual-Owner-Registration', 'form': form, 'message':message, 'values':values})

    return render(request, 'doormot_reg_users/individual_owner.html', {'title':'Individual-Owner-Registration', 'form': form})


# Private Organization Owner Registeration View
def private_organization_owner(request):
    form = Private_Organizations_Owner_Registeration_Form(request.POST)

    if request.method == 'POST':
        form = Private_Organizations_Owner_Registeration_Form(request.POST)
        
        if form.is_valid():
            profile = form.save()
            return redirect('doormot-reg-users-login')
        else:
            form = Private_Organizations_Owner_Registeration_Form(request.POST)
            errors = form.errors
            values = errors.values()
            message = "Error(s)!:"
            return render(request, 'doormot_reg_users/private_organization_owner.html', {'title':'Private-Organization-Owner-Registration', 'form': form, 'message':message, 'values':values})

   
    return render(request, 'doormot_reg_users/private_organization_owner.html', {'title':'Private-Organization-Owner-Registration', 'form': form})




















# SECTION: TENANTS
# Tenants views: Individual, Private Organization and Government


def individual_tenant(request):
    form = Individual_Tenant_Registration_Form(request.POST)

    if request.method == 'POST':
        form = Individual_Tenant_Registration_Form(request.POST)
        
        if form.is_valid():
            profile = form.save()
            return redirect('doormot-reg-users-login')
        else:
            form = Individual_Tenant_Registration_Form(request.POST)
            errors = form.errors
            values = errors.values()
            message = "Error(s)!:"
            return render(request, 'doormot_reg_users/tenant.html', {'title':'Individual-Tenant-registration', 'form': form, 'message':message, 'values':values})

    return render(request, 'doormot_reg_users/tenant.html', {'title':'Individual-Tenant-registration', 'form': form})


def private_organization_tenant(request):
    form = Private_Organization_Tenant_Registration_Form(request.POST)

    if request.method == 'POST':
        form = Private_Organization_Tenant_Registration_Form(request.POST)
        
        if form.is_valid():
            profile = form.save()
            return redirect('doormot-reg-users-login')
        else:
            form = Private_Organization_Tenant_Registration_Form(request.POST)
            errors = form.errors
            values = errors.values()
            message = "Error(s)!:"
            return render(request, 'doormot_reg_users/private_organization_tenant.html', {'title':'Private-Organization-Tenant-Registration', 'form': form, 'message':message, 'values':values})

    return render(request, 'doormot_reg_users/private_organization_tenant.html', {'title':'Private-Organization-Tenant-Registration', 'form': form})
















# SECTION: BUYERS
# Buyers Views: Individual, Private Organization and Government

# Individual Buyer Registeration View
def individual_buyer(request):
    form = Individual_buyer_registeration_form(request.POST)

    if request.method == 'POST':
        form = Individual_buyer_registeration_form(request.POST)
        
        if form.is_valid():
            profile = form.save()
            return redirect('doormot-reg-users-login')
        else:
            form = Individual_buyer_registeration_form(request.POST)
            errors = form.errors
            values = errors.values()
            message = "Error(s)!:"
            return render(request, 'doormot_reg_users/buyer.html', {'title':'Individual-Buyer-Registration', 'form': form, 'message':message, 'values':values})

    return render(request, 'doormot_reg_users/buyer.html', {'title':'Individual-Buyer-Registration', 'form': form})

# Private Organization Buyer Registeration View
def private_organization_buyer(request):
    form = Private_Organizations_Buyer_Registeration_Form(request.POST)

    if request.method == 'POST':
        form = Private_Organizations_Buyer_Registeration_Form(request.POST)
        
        if form.is_valid():
            profile = form.save()
            return redirect('doormot-reg-users-login')
        else:
            form = Private_Organizations_Buyer_Registeration_Form(request.POST)
            errors = form.errors
            values = errors.values()
            message = "Error(s)!:"
            return render(request, 'doormot_reg_users/private_organization_buyer.html', {'title':'Private-Organization-Buyer-Registration', 'form': form, 'message':message, 'values':values})

    return render(request, 'doormot_reg_users/private_organization_buyer.html', {'title':'Private-Organization-Buyer-Registration', 'form': form})





















# SECTION: AGENTS
# Agents Views: Individual, Private Organization and Government

# Official Agent Registeration View
def official_agent(request):
    form = Official_Agent_Registration_Form(request.POST)

    if request.method == 'POST':
        form = Official_Agent_Registration_Form(request.POST)

        if form.is_valid():
            profile = form.save()
            return redirect('doormot-reg-users-login')
        else:
            form = Official_Agent_Registration_Form(request.POST)
            errors = form.errors
            values = errors.values()
            message = "Error(s)!:"
            return render(request, 'doormot_reg_users/official_agent.html', {'title':'Official-Agent-registration', 'form':form, 'message':message, 'values':values})
        
    return render(request, 'doormot_reg_users/official_agent.html', {'title':'Official-Agent-registration', 'form':form})



# Independent Agent Registeration View
def independent_agent(request):
    form = Doormot_User_Independent_Agent_Registration_Form(request.POST)

    if request.method == 'POST':
        form = Doormot_User_Independent_Agent_Registration_Form(request.POST)

        if form.is_valid():
            profile = form.save()
            return redirect('doormot-reg-users-login')
        else:
            form = Doormot_User_Independent_Agent_Registration_Form(request.POST)
            errors = form.errors
            values = errors.values()
            message = "Error(s)!:"
            return render(request, 'doormot_reg_users/independent_agent.html', {'title':'Independent-Agent-registration', 'form':form, 'message':message, 'values':values})

            
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