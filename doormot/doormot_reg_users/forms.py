from django import forms
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, HTML, Submit
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Doormot_User_Individual_Owner, Doormot_User_Private_Organization_Owner, Doormot_User_Individual_Buyer, Doormot_User_Private_Organization_Buyer, Doormot_User_Individual_Tenant, Doormot_User_Private_Organization_Tenant, Doormot_User_Official_Agent, Doormot_User_Independent_Agent



# Section: OWNNERS
# Class for Individual, Private Organizations/Business and Government

class Individual_owner_registeration_form(UserCreationForm):
   
    password1 = forms.CharField(
        label = 'Password:',
        widget = forms.PasswordInput(attrs={'placeholder':'Password'}),
    )

    password2 = forms.CharField(
        label = 'Confirm Password',
        widget = forms.PasswordInput(attrs={'placeholder':'Confrim Password'}),
    )

    email = forms.EmailField(
        label = 'Email',
        widget = forms.TextInput(attrs={'placeholder':'Email'}),
        error_messages = {
            'required': 'Please enter your email address!',
            'invalid' : 'Please enter a valid email!',
        },
        required = True,
    )

    phone_number = forms.CharField(
        label = 'Phone Number',
        widget = forms.TextInput(attrs={'placeholder':'Phone Number'}),
        error_messages = {
            'required': 'Please enter your phone number address!',
        },
        required = True,
    )

    def cleaned_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered!")
        return email

    def cleaned_phone_number(self):
        email = self.cleaned_data['phone_number']
        if User.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("This email is Phone Number registered!")
        return phone_number

    class Meta:
        model = Doormot_User_Individual_Owner
        fields = ('username', 'password1', 'password2', 'email', 'phone_number')

# Individual Owner Form Class
class Individual_Owner_Login_Form(forms.Form):
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    helper = FormHelper()
    helper.add_input(Submit('submit', 'login'))


class Private_Organizations_Owner_Registeration_Form(UserCreationForm):
   
    password1 = forms.CharField(
        label = 'Password:',
        widget = forms.PasswordInput(attrs={'placeholder':'Password'}),
    )

    password2 = forms.CharField(
        label = 'Confirm Password',
        widget = forms.PasswordInput(attrs={'placeholder':'Confrim Password'}),
    )

    official_email = forms.EmailField(
        label = 'Email',
        widget = forms.TextInput(attrs={'placeholder':'Email'}),
        error_messages = {
            'required': 'Please enter your email address!',
            'invalid' : 'Please enter a valid email!',
        },
        required = True,
    )

    official_phone_number = forms.CharField(
        label = 'Phone Number',
        widget = forms.TextInput(attrs={'placeholder':'Phone Number'}),
        error_messages = {
            'required': 'Please enter your phone number address!',
        },
        required = True,
    )

    class Meta:
        model = Doormot_User_Private_Organization_Owner
        fields = ('username', 'password1',  'password2', 'official_email', 'official_phone_number', 'organization_type', 'official_registered_name', 'official_registered_number', 'website', 'certificate_image',)

    def clean_email(self):
        email = self.cleaned_data['email']
        if Doormot_User_Individual_Tenant.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered!")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if Doormot_User_Individual_Tenant.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("This phone number is already registered!")
        return phone_number

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match!")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class Private_Organizations_Owner_Login_Form(forms.Form):
    
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    helper = FormHelper()
    helper.add_input(Submit('submit', 'login'))


















# Section: BUYER
# Class for Individual, Private Organizations/Business and Government

class Individual_buyer_registeration_form(UserCreationForm):
   
    password1 = forms.CharField(
        label = 'Password:',
        widget = forms.PasswordInput(attrs={'placeholder':'Password'}),
    )

    password2 = forms.CharField(
        label = 'Confirm Password',
        widget = forms.PasswordInput(attrs={'placeholder':'Confrim Password'}),
    )

    email = forms.EmailField(
        label = 'Email',
        widget = forms.TextInput(attrs={'placeholder':'Email'}),
        error_messages = {
            'required': 'Please enter your email address!',
            'invalid' : 'Please enter a valid email!',
        },
        required = True,
    )

    phone_number = forms.CharField(
        label = 'Phone Number',
        widget = forms.TextInput(attrs={'placeholder':'Phone Number'}),
        error_messages = {
            'required': 'Please enter your phone number address!',
        },
        required = True,
    )

    def cleaned_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered!")
        return email

    def cleaned_phone_number(self):
        email = self.cleaned_data['phone_number']
        if User.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("This email is Phone Number registered!")
        return phone_number

    class Meta:
        model = Doormot_User_Individual_Buyer
        fields = ('username', 'password1', 'password2', 'email', 'phone_number')

class Individual_Buyer_Login_Form(forms.Form):
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    helper = FormHelper()
    helper.add_input(Submit('submit', 'login'))




class Private_Organizations_Buyer_Registeration_Form(UserCreationForm):
   
    password1 = forms.CharField(
        label = 'Password:',
        widget = forms.PasswordInput(attrs={'placeholder':'Password'}),
    )

    password2 = forms.CharField(
        label = 'Confirm Password',
        widget = forms.PasswordInput(attrs={'placeholder':'Confrim Password'}),
    )

    official_email = forms.EmailField(
        label = 'Email',
        widget = forms.TextInput(attrs={'placeholder':'Email'}),
        error_messages = {
            'required': 'Please enter your email address!',
            'invalid' : 'Please enter a valid email!',
        },
        required = True,
    )

    official_phone_number = forms.CharField(
        label = 'Phone Number',
        widget = forms.TextInput(attrs={'placeholder':'Phone Number'}),
        error_messages = {
            'required': 'Please enter your phone number address!',
        },
        required = True,
    )

    class Meta:
        model = Doormot_User_Private_Organization_Buyer
        fields = ('username', 'password1',  'password2', 'official_email', 'official_phone_number', 'organization_type', 'official_registered_name', 'official_registered_number', 'website', 'certificate_image',)

    def clean_email(self):
        email = self.cleaned_data['email']
        if Doormot_User_Individual_Tenant.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered!")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if Doormot_User_Individual_Tenant.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("This phone number is already registered!")
        return phone_number

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match!")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class Private_Organizations_Buyer_Login_Form(forms.Form):
    
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    helper = FormHelper()
    helper.add_input(Submit('submit', 'login'))









# Section: TENANTS
# Class for Individual, Private Organizations/Business and Government

class Individual_Tenant_Registration_Form(UserCreationForm):

    password1 = forms.CharField(
        label = 'Password:',
        widget = forms.PasswordInput(attrs={'placeholder':'Password'}),
    )

    password2 = forms.CharField(
        label = 'Confirm Password',
        widget = forms.PasswordInput(attrs={'placeholder':'Confrim Password'}),
    )

    email = forms.EmailField(
        label = 'Email',
        widget = forms.TextInput(attrs={'placeholder':'Email'}),
        error_messages = {
            'required': 'Please enter your email address!',
            'invalid' : 'Please enter a valid email!',
        },
        required = True,
    )

    phone_number = forms.CharField(
        label = 'Phone Number',
        widget = forms.TextInput(attrs={'placeholder':'Phone Number'}),
        error_messages = {
            'required': 'Please enter your phone number address!',
        },
        required = True,
    )

    class Meta:
        model = Doormot_User_Individual_Tenant
        fields = ('username', 'password1',  'password2', 'email', 'phone_number')

    def clean_email(self):
        email = self.cleaned_data['email']
        if Doormot_User_Individual_Tenant.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered!")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if Doormot_User_Individual_Tenant.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("This phone number is already registered!")
        return phone_number

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match!")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class Individual_Tenant_Login_Form(forms.Form):
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    helper = FormHelper()
    helper.add_input(Submit('submit', 'login'))


        
# Private Organizations Agent Registeration Form:
class Private_Organization_Tenant_Registration_Form(UserCreationForm):

    password1 = forms.CharField(
        label = 'Password:',
        widget = forms.PasswordInput(attrs={'placeholder':'Password'}),
    )

    password2 = forms.CharField(
        label = 'Confirm Password',
        widget = forms.PasswordInput(attrs={'placeholder':'Confrim Password'}),
    )

    official_email = forms.EmailField(
        label = 'Email',
        widget = forms.TextInput(attrs={'placeholder':'Email'}),
        error_messages = {
            'required': 'Please enter your email address!',
            'invalid' : 'Please enter a valid email!',
        },
        required = True,
    )

    official_phone_number = forms.CharField(
        label = 'Phone Number',
        widget = forms.TextInput(attrs={'placeholder':'Phone Number'}),
        error_messages = {
            'required': 'Please enter your phone number address!',
        },
        required = True,
    )

    class Meta:
        model = Doormot_User_Private_Organization_Tenant
        fields = ('username', 'password1',  'password2', 'official_email', 'official_phone_number', 'organization_type', 'official_registered_name', 'official_registered_number', 'office_address', 'website', 'certificate_image',)

    def clean_email(self):
        email = self.cleaned_data['email']
        if Doormot_User_Individual_Tenant.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered!")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if Doormot_User_Individual_Tenant.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("This phone number is already registered!")
        return phone_number

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match!")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class Private_Organization_Tenant_Login_Form(forms.Form):
    
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    helper = FormHelper()
    helper.add_input(Submit('submit', 'login'))




# Section: AGENTS
# Class for Official and Independent

# Official Agent Registeration Form:
class Official_Agent_Registration_Form(UserCreationForm):

    password1 = forms.CharField(
        label = 'Password:',
        widget = forms.PasswordInput(attrs={'placeholder':'Password'}),
    )

    password2 = forms.CharField(
        label = 'Confirm Password',
        widget = forms.PasswordInput(attrs={'placeholder':'Confrim Password'}),
    )

    email = forms.EmailField(
        label = 'Email',
        widget = forms.TextInput(attrs={'placeholder':'Email'}),
        error_messages = {
            'required': 'Please enter your email address!',
            'invalid' : 'Please enter a valid email!',
        },
        required = True,
    )

    phone_number = forms.CharField(
        label = 'Phone Number',
        widget = forms.TextInput(attrs={'placeholder':'Phone Number'}),
        error_messages = {
            'required': 'Please enter your phone number address!',
        },
        required = True,
    )

    class Meta:
        model = Doormot_User_Official_Agent
        fields = ('username', 'password1',  'password2', 'email', 'phone_number')


    def clean_email(self):
        email = self.cleaned_data['email']
        if Doormot_User_Official_Agent.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered!")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if Doormot_User_Official_Agent.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("This phone number is already registered!")
        return phone_number

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

# Official Agent Login Form Class
class Official_Agent_Login_Form(forms.Form):
    
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    
    helper = FormHelper()
    helper.add_input(Submit('submit', 'login'))







# Independent Agent Registeration Form:
class Doormot_User_Independent_Agent_Registration_Form(UserCreationForm):

    password1 = forms.CharField(
        label = 'Password:',
        widget = forms.PasswordInput(attrs={'placeholder':'Password', "class":"w-64 p-2 border rounded-md"}),
    )

    password2 = forms.CharField(
        label = 'Confirm Password',
        widget = forms.PasswordInput(attrs={'placeholder':'Confrim Password', 'class':'w-64 p-2 border rounded-md'}),
    )

    email = forms.EmailField(
        label = 'Email',
        widget = forms.TextInput(attrs={'placeholder':'Email', 'class':'w-64 p-2 border rounded-md'}),
        error_messages = {
            'required': 'Please enter your email address!',
            'invalid' : 'Please enter a valid email!',
        },
        required = True,
    )

    phone_number = forms.CharField(
        label = 'Phone Number',
        widget = forms.TextInput(attrs={'placeholder':'Phone Number', 'class':'w-64 p-2 border rounded-md'}),
        error_messages = {
            'required': 'Please enter your phone number address!',
        },
        required = True,
    )


    class Meta:
        model = Doormot_User_Independent_Agent
        fields = ('username', 'password1',  'password2', 'email', 'phone_number')

    def clean_email(self):
        email = self.cleaned_data['email']
        if Doormot_User_Official_Agent.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered!")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if Doormot_User_Official_Agent.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("This phone number is already registered!")
        return phone_number

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class Doormot_User_Independent_Agent_Login_Form(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    helper = FormHelper()
    helper.add_input(Submit('submit', 'login'))