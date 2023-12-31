from django.utils import timezone
from datetime import timedelta
import logging
import random
import string
import secrets
import hashlib
import binascii
from django.dispatch import Signal, receiver

# from django.core.mail import send_mail
# from django_otp.plugins.otp_totp.models import TOTPDevice
# from twilio.rest import Client
# from doormot_app.doormot_app_modules import return_user_object
# import smtplib
# from email.mine.text import MIMEText
# from email.mine.multipart import MIMEMultipart

logger = logging.getLogger(__name__)






# CAUTION!! Don't TAMPER: Currently in use
# Function: To generate random integer, or four-letter-random-word
class rand():
    def generate_random_number(self):
        return random.randint(1000, 9999)
    try:

        def generate(self):
            alphabet = string.ascii_uppercase
            combination = random.sample(alphabet, 4)
            return ''.join(combination)

        def alphanumeric(self):
            random_number = self.generate_random_number()
            random_alphabet = self.generate()
            rad = f'{random_number}{random_alphabet}'
            return rad
    except Exception as e:
        logger.exception("There was an error during generating random number: %s", e)

# Create a custom Signal instance 
send_signal = Signal()


# Type: Class
class generate_hashed_secret_code:
    def __init__(self, token_lenght, hash_iterations):
        self.token_lenght = token_lenght
        self.hash_iterations = hash_iterations

    try:
        def generate_hexadeci_code(self):
            return secrets.token_hex(self.token_lenght)

        def generate_salt(self):
            return secrets.token_bytes(16)

        def hash_code(self, secret_code, salt):
            hashed_code = hashlib.pbkdf2_hmac('sha256', secret_code.encode('utf-8'), salt, self.hash_iterations)
            return binascii.hexlify(hashed_code).decode()
    except Exception as e:
        logger.exception("There was an error during hashing: %s", e)


class locked_account_time_difference:
    def __init__(self, start_time, lock_threshold_by_hours):
        self.start_time = start_time
        self.lock_threshold_by_hours = lock_threshold_by_hours
    try:
        def calculate_countdown(self):
            current_date_time = timezone.now()

            time_difference = current_date_time - self.start_time

            target_lock_threshold = timedelta(hours=self.lock_threshold_by_hours)

            if time_difference < target_lock_threshold:
                return False
            else:
                return True

        def calculate_countdown_remaining(self):
            current_date_time = timezone.now()

            time_difference = current_date_time - self.start_time

            target_lock_threshold = timedelta(hours=self.lock_threshold_by_hours)

            remaining_time = target_lock_threshold - time_difference

            remaining_time = max(remaining_time, timedelta(0))

            return remaining_time
    except Exception as e:
        logger.exception("There was an exception: %s", e)



# Global receiver function for signals
# @receiver(send_signal)
# def send_unhashed_recovery_code_to_mail(sender, unhashed_recovery_code, **kwargs):
#     send_mail(subject, body, receipient)

# def send_mail(subject, body, receipient):
#     smtp_server = 'smpt.gmail.com'
#     smpt_port = 587
#     smpt_username = 'Doormot'
#     smpt_password = 'password'

#     from_email = 'doormot@gmail.com'
#     to_email = receipient

#     message = MIMEMultipart()
#     message['from'] = from_email
#     message['To'] = to_email
#     message['Subject'] = subject

#     message.attach(MIMEText(body, 'plain'))

#     with smtplib.SMPT(smtp_server, smpt_port) as server:
#         server.starttls()
#         server.login(smpt_username, smpt_password)
#         server.sendmail(from_email, to_email, message.as_string())

# class send_otp_code():
#     self.device = TOTPDevice.objects.get(user=user, confirmed=True)
#     self.otp_code = device.generate_otp()
    
#     def send_otp_email(self, user, otp_method):
#         try:
#             if otp_method == "email":
#                 subject = 'Your OTP for login'
#                 message = f'Your login OTP is: {self.otp_code}'
#                 from_email = 'from@example.com'  # Set your email address
#                 recipient_list = [user.email]
#                 send_mail(subject, message, from_email, recipient_list, fail_silently=False)
#                 return True
#         except Exception as e:
#             logger.exception("There was an error: %s", e)
#             return False


#     def send_otp_sms(self, user, otp_method):
#         # Twilio credentials
#         account_sid = 'your_account_sid'
#         auth_token = 'your_auth_token'
#         twilio_phone_number = 'your_twilio_phone_number'

#         client = Client(account_sid, auth_token)

#         try:
#             if otp_method == "sms":
#                 message = client.messages.create(
#                     body=f"Your OTP for login is: {self.otp_code}",
#                     from_=twilio_phone_number,
#                     to=user.phone_number
#                     )
#                 return True
#         except Exception as e:
#             logger.exception("There was an error: %s", e)
#             return False


# def send_otp_code():
#     device = TOTPDevice.objects.get(user=user, confirmed=True)
#     otp_code = device.generate_otp()
        
        
#     # Your Twilio credentials
#     account_sid = 'your_account_sid'
#     auth_token = 'your_auth_token'
#     twilio_phone_number = 'your_twilio_phone_number'

#     client = Client(account_sid, auth_token)

#     if otp_method == "email":
#         try:
#             subject = 'Your OTP for login'
#             message = f'Your login OTP is: {otp_code}'
#             from_email = 'from@example.com'  # Set your email address
#             recipient_list = [user.email]
#             send_mail(subject, message, from_email, recipient_list, fail_silently=False)
#             return True
#         except Exception as e:
#             logger.exception("There was an error: %s", e)
#             return False

#     if otp_method == "sms":
#         try:
#             message = client.messages.create(
#             body=f"Your OTP for login is: {otp_code}",
#             from_=twilio_phone_number,
#             to=user.phone_number
#             )
#             return True
#         except Exception as e:
#             logger.exception("There was an error: %s", e)
#             return False

            

# def otp_verification(user, otp_code):
#     first_error_message = "Invalid OTP"
#     second_error_message = "Expired OTP"
#     try:
#         device = TOTPDevice.objects.get(user=user, confirmed=True)
#         if device.verify_token(otp_code):
#             if device.time_until_next_token() > timezone.timedelta(seconds=0):
#                 return True
#             return second_error_message
#         return first_error_message
#     except TOTPDevice.DoesNotExist as e:
#             logger.exception("There was an error: %s", e)
#             return False









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

# class DoormotCustomLoginView(LoginView):
#     def get(self, request):
#         name = None
#         user_type = request.GET.get('user_type', 'Individual_owner')

#         request.session['user_type'] = user_type
#         name = user_type
        
#         # Determine user type and render the appropriate login form
#         if user_type == 'Individual_owner':
#             form = Individual_Owner_Login_Form()
#         if user_type == 'Private_org_owner':
#             form = Private_Organizations_Owner_Login_Form()

        
#         if user_type == 'Individual_buyer':
#             form = Individual_Buyer_Login_Form()        
#         if user_type == 'Private_org_buyer':
#             form = Private_Organizations_Buyer_Login_Form()
        
#         if user_type == 'Individual_tenant':
#             form = Individual_Tenant_Login_Form()
#         if user_type == 'Private_org_tenant':
#             form = Private_Organization_Tenant_Login_Form()

#         if user_type == 'Official_agent':
#             form = Official_Agent_Login_Form()
#         if user_type == 'Independent_agent':
#             form = Doormot_User_Independent_Agent_Login_Form()

#         return render(request, 'doormot_reg_users/login.html', {"title":"Login", 'form':form, 'name':name})

#     def post(self, request):
#         email = request.POST.get('email')
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         otp_method = request.POST.get('otp_method')
#         request.session['otp_method'] = otp_method
#         user_type = request.session.get('user_type')

#         # Authenticate user based on the provided credentials
#         user = DoormotCustomUserBackend.authenticate(self, request=request, username=username, email=email, password=password, user_type=user_type, backend = 'doormot.doormot_reg_users.backends.DoormotCustomUserBackend')

#         if user is not None:            
#             if user.is_active:
#                 request.session['user'] = user.pk
#                 if send_otp_code(user, otp_method):
#                     return render(request, 'doormot_reg_users/otp_verification.html')
#             else:
#                 return render (request, 'doormot_reg_users/account_disabled.html', {"title":"Account Disabled", "user":user})
#         else:
#             return render (request, 'doormot_reg_users/login_failed.html', {"title":"Login Failed", "user":user})
        



# def Login_OTP_Verification_View(request):
#     if request.method == 'POST':
#         otp_method = request.session.get('otp_method')
#         user_pk = request.session.get('user_pk')
#         user_type = request.session.get('user_type')
#         otp_code = request.POST.get('otp_code')
#         user = return_user_object(user_pk, user_type)
#         try:
#             verification = otp_verification(user, otp_code)
#             if verification:
#                 user.backend = 'doormot.doormot_reg_users.backends.DoormotCustomUserBackend'
#                 login(request, user)
#                 return render (request, 'doormot_app/home.html', {"title":"Home", "user":user})
#             elif verification == first_error_message:
#                 return render(request, 'otp_verification.html', {'error_message': first_error_message})
#             elif verification == second_error_message:
#                 logout(request)
#                 return redirect('doormot-reg-users-login')
#             else:
#                 logout(request)
#                 return redirect('doormot-reg-users-login')
#         except Exception as e:
#             logger.exception("There was an error: %s", e)
#             logout(request)
#             return redirect('doormot-reg-users-login')




