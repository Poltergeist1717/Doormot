from django import forms
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, HTML
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Doormot_User_Individual_Tenant, Doormot_User_Private_Organization_Tenant, Doormot_User_Official_Agent, Doormot_User_Independent_Agent




# Section: AGENTS
# Class for Official and Independent

# Official Agent Registeration Form:
class Official_Agent_Profile_Update_Form(forms.ModelForm):

    password1 = forms.CharField(
        label = 'Password:',
        widget = forms.PasswordInput(attrs={'placeholder':'Password'}),
    )

    password2 = forms.CharField(
        label = 'Confirm Password',
        widget = forms.PasswordInput(attrs={'placeholder':'Confrim Password'}),
    )

    agent_gender = forms.ChoiceField(
        label = 'Gender',
        choices = Doormot_User_Official_Agent.GENDER_CHOICES,
        widget = forms.Select(attrs={'class': 'relative'}),
        error_messages = {
            'required': 'Gender choice is required!',
        },
        required = True,
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

    state_of_origin = forms.CharField(
        label = 'State Of Origin',
        widget = forms.TextInput(attrs={'placeholder':'State Of Origin'}),
        error_messages = {
            'required':'Please enter your state of origin!'
        },
        required = True
    )

    town_of_origin = forms.CharField(
        label = 'Town Of Origin',
        widget = forms.TextInput(attrs={'placeholder':'Town Of Origin'}),
        error_messages = {
            'required':'Please enter your town of origin!'
        },
        required = True
    )

    local_government_of_origin = forms.CharField(
        label = 'Local Government Of Origin',
        widget = forms.TextInput(attrs={'placeholder':'Local Government Of Origin'}),
        error_messages = {
            'required':'Please enter your local government of origin!'
        },
        required = True
    )


    state_of_residence = forms.CharField(
        label = 'State Of Residence',
        widget = forms.TextInput(attrs={'placeholder':'State Of Residence'}),
        error_messages = {
            'required':'Please enter your state of residence!'
        },
        required = True
    )

    town_of_residence = forms.CharField(
        label = 'Town Of Residence',
        widget = forms.TextInput(attrs={'placeholder':'Town Of Residence'}),
        error_messages = {
            'required':'Please enter your town of residence!'
        },
        required = True
    )

    local_government_of_residence = forms.CharField(
        label = 'Local Government Of Residence',
        widget = forms.TextInput(attrs={'placeholder':'Local Government Of Residence'}),
        error_messages = {
            'required':'Please enter your local government of residence!'
        },
        required = True
    )

    date_of_birth = forms.DateField(
        label = 'Date Of Birth',
        widget = forms.DateInput(attrs={'placeholder':'Date Of Birth'}),
        error_messages = {
            'required':'Please enter your date of birth!'
        },
        required = True
    )

    class Meta:
        model = Doormot_User_Official_Agent
        fields = ('username', 'password1',  'password2', 'first_name', 'middle_name', 'last_name' , 'agent_gender', 'email', 'phone_number', 'state_of_origin', 'town_of_origin', 'local_government_of_origin', 'state_of_residence', 'town_of_residence', 'local_government_of_residence', 'date_of_birth', 'image', 'video')


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

class Official_Agent_Guarantor_Profile_Update_Form(forms.ModelForm):

    guarantor_gender = forms.ChoiceField(
        label = 'Gender',
        choices = Doormot_User_Official_Agent.GENDER_CHOICES,
        widget = forms.Select(attrs={'class': 'relative'}),
        error_messages = {
            'required': 'Gender choice is required!',
        },
        required = True,
        )

    guarantor_email = forms.EmailField(
        label = 'Email',
        widget = forms.TextInput(attrs={'placeholder':'Email'}),
        error_messages = {
            'required': 'Please enter your email address!',
            'invalid' : 'Please enter a valid email!',
        },
        required = True,
    )

    guarantor_phone_number = forms.CharField(
        label = 'Phone Number',
        widget = forms.TextInput(attrs={'placeholder':'Phone Number'}),
        error_messages = {
            'required': 'Please enter your phone number address!',
        },
        required = True,
    )

    guarantor_state_of_origin = forms.CharField(
        label = 'State Of Origin',
        widget = forms.TextInput(attrs={'placeholder':'State Of Origin'}),
        error_messages = {
            'required':'Please enter your state of origin!'
        },
        required = True
    )

    guarantor_town_of_origin = forms.CharField(
        label = 'Town Of Origin',
        widget = forms.TextInput(attrs={'placeholder':'Town Of Origin'}),
        error_messages = {
            'required':'Please enter your town of origin!'
        },
        required = True
    )

    guarantor_government_of_origin = forms.CharField(
        label = 'Local Government Of Origin',
        widget = forms.TextInput(attrs={'placeholder':'Local Government Of Origin'}),
        error_messages = {
            'required':'Please enter your local government of origin!'
        },
        required = True
    )


    guarantor_state_of_residence = forms.CharField(
        label = 'State Of Residence',
        widget = forms.TextInput(attrs={'placeholder':'State Of Residence'}),
        error_messages = {
            'required':'Please enter your state of residence!'
        },
        required = True
    )

    guarantor_town_of_residence = forms.CharField(
        label = 'Town Of Residence',
        widget = forms.TextInput(attrs={'placeholder':'Town Of Residence'}),
        error_messages = {
            'required':'Please enter your town of residence!'
        },
        required = True
    )

    guarantor_local_government_of_residence = forms.CharField(
        label = 'Local Government Of Residence',
        widget = forms.TextInput(attrs={'placeholder':'Local Government Of Residence'}),
        error_messages = {
            'required':'Please enter your local government of residence!'
        },
        required = True
    )

    guarantor_date_of_birth = forms.DateField(
        label = 'Date Of Birth',
        widget = forms.DateInput(attrs={'placeholder':'Date Of Birth'}),
        error_messages = {
            'required':'Please enter your date of birth!'
        },
        required = True
    )

    class Meta:
        model = Doormot_User_Official_Agent
        fields = ('guarantor_email', 'guarantor_phone_number', 'guarantor_first_name', 'guarantor_middle_name', 'guarantor_last_name', 'guarantor_gender', 'guarantor_state_of_origin', 'guarantor_town_of_origin', 'guarantor_local_government_of_origin', 'guarantor_state_of_residence', 'guarantor_town_of_residence', 'guarantor_local_government_of_residence', 'guarantor_date_of_birth', 'guarantor_image')


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

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user


class Official_Agent_Next_Of_Kin_Profile_Update_Form(forms.ModelForm):

    next_of_kin_gender = forms.ChoiceField(
        label = 'Gender',
        choices = Doormot_User_Official_Agent.GENDER_CHOICES,
        widget = forms.Select(attrs={'class': 'relative'}),
        error_messages = {
            'required': 'Gender choice is required!',
        },
        required = True,
        )

    next_of_kin_email = forms.EmailField(
        label = 'Email',
        widget = forms.TextInput(attrs={'placeholder':'Email'}),
        error_messages = {
            'required': 'Please enter your email address!',
            'invalid' : 'Please enter a valid email!',
        },
        required = True,
    )

    next_of_kin_phone_number = forms.CharField(
        label = 'Phone Number',
        widget = forms.TextInput(attrs={'placeholder':'Phone Number'}),
        error_messages = {
            'required': 'Please enter your phone number address!',
        },
        required = True,
    )

    next_of_kin_state_of_origin = forms.CharField(
        label = 'State Of Origin',
        widget = forms.TextInput(attrs={'placeholder':'State Of Origin'}),
        error_messages = {
            'required':'Please enter your state of origin!'
        },
        required = True
    )

    next_of_kin_town_of_origin = forms.CharField(
        label = 'Town Of Origin',
        widget = forms.TextInput(attrs={'placeholder':'Town Of Origin'}),
        error_messages = {
            'required':'Please enter your town of origin!'
        },
        required = True
    )

    next_of_kin_local_government_of_origin = forms.CharField(
        label = 'Local Government Of Origin',
        widget = forms.TextInput(attrs={'placeholder':'Local Government Of Origin'}),
        error_messages = {
            'required':'Please enter your local government of origin!'
        },
        required = True
    )


    next_of_kin_state_of_residence = forms.CharField(
        label = 'State Of Residence',
        widget = forms.TextInput(attrs={'placeholder':'State Of Residence'}),
        error_messages = {
            'required':'Please enter your state of residence!'
        },
        required = True
    )

    next_of_kin_town_of_residence = forms.CharField(
        label = 'Town Of Residence',
        widget = forms.TextInput(attrs={'placeholder':'Town Of Residence'}),
        error_messages = {
            'required':'Please enter your town of residence!'
        },
        required = True
    )

    next_of_kin_local_government_of_residence = forms.CharField(
        label = 'Local Government Of Residence',
        widget = forms.TextInput(attrs={'placeholder':'Local Government Of Residence'}),
        error_messages = {
            'required':'Please enter your local government of residence!'
        },
        required = True
    )

    next_of_kin_date_of_birth = forms.DateField(
        label = 'Date Of Birth',
        widget = forms.DateInput(attrs={'placeholder':'Date Of Birth'}),
        error_messages = {
            'required':'Please enter your date of birth!'
        },
        required = True
    )

    class Meta:
        model = Doormot_User_Official_Agent
        fields = ('next_of_kin_email', 'next_of_kin_phone_number', 'next_of_kin_first_name', 'next_of_kin_middle_name', 'next_of_kin_last_name', 'next_of_kin_gender', 'next_of_kin_state_of_origin', 'next_of_kin_town_of_origin', 'next_of_kin_local_government_of_origin', 'next_of_kin_state_of_residence', 'next_of_kin_town_of_residence', 'next_of_kin_local_government_of_residence', 'next_of_kin_date_of_birth', 'next_of_kin_image')


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

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user








# Independent Agent Registeration Form:
class Doormot_User_Independent_Agent_Profile_Update_Form(UserCreationForm):

    password1 = forms.CharField(
        label = 'Password:',
        widget = forms.PasswordInput(attrs={'placeholder':'Password', "class":"w-64 p-2 border rounded-md"}),
    )

    password2 = forms.CharField(
        label = 'Confirm Password',
        widget = forms.PasswordInput(attrs={'placeholder':'Confrim Password', 'class':'w-64 p-2 border rounded-md'}),
    )


    # agent_gender = forms.ChoiceField(
    #     label = 'Gender',
    #     choices = Doormot_User_Official_Agent.GENDER_CHOICES,
    #     widget = forms.Select(attrs={'class': 'relative', 'class':'w-64 p-2 border rounded-md'}),
    #     error_messages = {
    #         'required': 'Gender choice is required!',
    #     },
    #     required = True,
    #     )

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

    state_of_origin = forms.CharField(
        label = 'State Of Origin',
        widget = forms.TextInput(attrs={'placeholder':'State Of Origin', 'class':'w-64 p-2 border rounded-md'}),
        error_messages = {
            'required':'Please enter your state of origin!'
        },
        required = True
    )

    town_of_origin = forms.CharField(
        label = 'Town Of Origin',
        widget = forms.TextInput(attrs={'placeholder':'Town Of Origin', 'class':'w-64 p-2 border rounded-md'}),
        error_messages = {
            'required':'Please enter your town of origin!'
        },
        required = True
    )

    local_government_of_origin = forms.CharField(
        label = 'Local Government Of Origin',
        widget = forms.TextInput(attrs={'placeholder':'Local Government Of Origin', 'class':'w-64 p-2 border rounded-md'}),
        error_messages = {
            'required':'Please enter your local government of origin!'
        },
        required = True
    )


    state_of_residence = forms.CharField(
        label = 'State Of Residence',
        widget = forms.TextInput(attrs={'placeholder':'State Of Residence', 'class':'w-64 p-2 border rounded-md'}),
        error_messages = {
            'required':'Please enter your state of residence!'
        },
        required = True
    )

    town_of_residence = forms.CharField(
        label = 'Town Of Residence',
        widget = forms.TextInput(attrs={'placeholder':'Town Of Residence', 'class':'w-64 p-2 border rounded-md'}),
        error_messages = {
            'required':'Please enter your town of residence!'
        },
        required = True
    )

    local_government_of_residence = forms.CharField(
        label = 'Local Government Of Residence',
        widget = forms.TextInput(attrs={'placeholder':'Local Government Of Residence', 'class':'w-64 p-2 border rounded-md'}),
        error_messages = {
            'required':'Please enter your local government of residence!'
        },
        required = True
    )

    date_of_birth = forms.DateField(
        label = 'Date Of Birth',
        widget = forms.DateInput(attrs={'placeholder':'Date Of Birth', 'class':'w-64 p-2 border rounded-md'}),
        error_messages = {
            'required':'Please enter your date of birth!'
        },
        required = True
    )


    class Meta:
        model = Doormot_User_Independent_Agent
        fields = ('username', 'password1',  'password2', 'first_name', 'middle_name', 'last_name', 'agent_gender', 'email', 'phone_number', 'state_of_origin', 'town_of_origin', 'local_government_of_origin', 'origin_home_address', 'state_of_residence', 'town_of_residence', 'local_government_of_residence', 'current_home_address', 'date_of_birth', 'image', 'video',
                'next_of_kin_email', 'next_of_kin_phone_number', 'next_of_kin_first_name', 'next_of_kin_middle_name', 'next_of_kin_last_name', 'next_of_kin_gender', 'next_of_kin_state_of_origin', 'next_of_kin_town_of_origin', 'next_of_kin_local_government_of_origin', 'next_of_kin_state_of_residence', 'next_of_kin_town_of_residence', 'next_of_kin_local_government_of_residence', 'next_of_kin_current_home_address', 'next_of_kin_current_office_address', 'next_of_kin_date_of_birth', 'next_of_kin_image',
                'guarantor_email', 'guarantor_phone_number', 'guarantor_first_name', 'guarantor_middle_name', 'guarantor_last_name', 'guarantor_gender', 'guarantor_state_of_origin', 'guarantor_town_of_origin', 'guarantor_local_government_of_origin', 'guarantor_state_of_residence', 'guarantor_town_of_residence', 'guarantor_local_government_of_residence', 'guarantor_current_home_address', 'guarantor_current_office_address', 'guarantor_date_of_birth', 'guarantor_image',
         )


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