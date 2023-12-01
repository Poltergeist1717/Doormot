from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Permission, Group
from django.contrib.auth import validators
from django.utils import timezone
from django.core.exceptions import ValidationError
from .doormot_reg_modules import rand
from django.contrib.contenttypes.fields import GenericRelation




def validate_video_size(value):
    # Specify the maximum file size (e.g., 10MB)
    max_size = 10 * 1024 * 1024  # 10MB in bytes

    if value.size > max_size:
        raise ValidationError(_('File size cannot exceed 10MB.'))



class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, phone_number=None):
        if not email:
            raise ValueError('The Email field must be filled!')
        user = self.model(username=username, email=self.normalize_email(email), phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user_custom_base_user(self, username, email, password=None, phone_number=None):
        if not email:
            raise ValueError('The Email field must be filled!')

        user = self.model(username=username, email=self.normalize_email(email), phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)

        
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_superuser(username, email, password, **extra_fields)



















# SECTION: OWNERS
# Owners models: Individual, Private Organization and Government


# INDIVIDUAL OWNER MODEL
class Doormot_User_Individual_Owner_Details(models.Model):
 
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
        ('U', 'Prefer not to say'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('S', 'Single'),
        ('M', 'Married'),
        ('E', 'Engaged'),
        ('D', 'Divorced'),
        ('W', 'Widowed'),
        ('U', 'Prefer not to say'),
    ]

    EDUCATION_LEVEL_CHOICES = [
        ('H', 'High School Graduate'),
        ('G', 'University Graduate'),
        ('U', 'Undergraduate'),
        ('A', 'Apprenticeship Graduate'),
        ('U', 'Prefer not to say'),
    ]

    EMPLOYMENT_STATUS_CHOICES = [
        ('E', 'Employed'),
        ('U', 'Unemployed'),
        ('S', 'Self Employed'),
        ('U', 'Prefer not to say'),
    ]

    gender = models.CharField(null=False, blank=False, max_length=40, choices=GENDER_CHOICES,  default=None)
    education_level = models.CharField(null=False, blank=False, max_length=40, choices=EDUCATION_LEVEL_CHOICES,  default=None)
    marital_status = models.CharField(null=False, blank=False, max_length=40, choices=MARITAL_STATUS_CHOICES,  default=None)
    employment_status = models.CharField(null=False, blank=False, max_length=40, choices=EMPLOYMENT_STATUS_CHOICES, default=None)


    image = models.ImageField(upload_to='individual_owner_images/',  default=None)
    video = models.FileField(upload_to='individual_owner_videos/', validators=[validate_video_size], default=None)

    first_name = models.CharField(null=False, blank=False, max_length=40, default=None)
    middle_name = models.CharField(null=True, blank=True, max_length=40, default=None)
    last_name = models.CharField(null=False, blank=False, max_length=40, default=None)

    state_of_origin = models.CharField(null=False, blank=False, max_length=40, default=None)
    town_of_origin = models.CharField(null=False, blank=False, max_length=40, default=None)
    local_government_of_origin = models.CharField(null=False, blank=False, max_length=40, default=None)
    origin_home_address = models.CharField(null=False, blank=False, max_length=200, default=None)

    state_of_residence = models.CharField(null=False, blank=False, max_length=40, default=None)
    town_of_residence = models.CharField(null=False, blank=False, max_length=40, default=None)
    local_government_of_residence = models.CharField(null=False, blank=False, max_length=40, default=None)
    current_home_address = models.CharField(null=False, blank=False, max_length=200, default=None)

    date_of_birth = models.DateField(null=False, blank=False, default=timezone.now)
    


class Doormot_User_Individual_Owner(AbstractBaseUser, PermissionsMixin):
    individual_tenant_details = models.OneToOneField(Doormot_User_Individual_Owner_Details, on_delete=models.CASCADE, null=True, blank=True)

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name = 'user permissions',
        blank = True,
        related_name = 'Doormot_User_Individual_Owner_Perm',
    )

    groups = models.ManyToManyField(
        Group, 
        verbose_name='groups', 
        blank=True, 
        related_name='individual_owner_groups'
    )

    user_id = models.CharField(max_length=50, unique=True, default=None)
    false_log_count = models.PositiveIntegerField(null=True, default=None)
    currently_logged_in = models.BooleanField(null=True, default=False)

    to_let_listings = GenericRelation('doormot_property_listing.To_Let_Listed_Properties')
    for_sale_listings = GenericRelation('doormot_property_listing.For_Sale_Listed_Properties')

    username = models.CharField(max_length=30, unique=True, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=False, blank=False, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            current_date = timezone.now().date()
            random = rand()
            random_alphanumeric = random.alphanumeric()
            random_int = random.generate_random_number()

            self.user_id = f"IND/OWN/{random_int}/{random_alphanumeric}/{current_date}"
        super().save(*args, **kwargs)

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'

    class Meta:
        app_label = 'doormot_reg_users'

    def __str__(self):
        return self.username


class Doormot_User_Individual_Owner_Next_Of_Kin(models.Model):
    
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
        ('U', 'Prefer not to say'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('S', 'Single'),
        ('M', 'Married'),
        ('E', 'Engaged'),
        ('D', 'Divorced'),
        ('W', 'Widowed'),
        ('U', 'Prefer not to say'),
    ]

    EDUCATION_LEVEL_CHOICES = [
        ('H', 'High School Graduate'),
        ('G', 'University Graduate'),
        ('U', 'Undergraduate'),
        ('A', 'Apprenticeship Graduate'),
        ('U', 'Prefer not to say'),
    ]

    EMPLOYMENT_STATUS_CHOICES = [
        ('E', 'Employed'),
        ('U', 'Unemployed'),
        ('S', 'Self Employed'),
        ('U', 'Prefer not to say'),
    ]

    gender = models.CharField(null=False, blank=False, max_length=40, choices=GENDER_CHOICES,  default=None)
    education_level = models.CharField(null=False, blank=False, max_length=40, choices=EDUCATION_LEVEL_CHOICES,  default=None)
    marital_status = models.CharField(null=False, blank=False, max_length=40, choices=MARITAL_STATUS_CHOICES,  default=None)
    employment_status = models.CharField(null=False, blank=False, max_length=40, choices=EMPLOYMENT_STATUS_CHOICES, default=None)


    user = models.ForeignKey(Doormot_User_Individual_Owner, on_delete=models.CASCADE, related_name='individual_owner_next_of_kin')
    
    email = models.EmailField(unique=True, null=False, blank=False, default=None)
    phone_number = models.CharField(unique=True, null=False, blank=False, max_length=15, default=None)

    image = models.ImageField(upload_to='individual_tenant_next_of_kin_images/', default=None)

    first_name = models.CharField(null=False, blank=False, max_length=40, default=None)
    middle_name = models.CharField(null=True, blank=True, max_length=40, default=None)
    last_name = models.CharField(null=False, blank=False, max_length=40, default=None)

    state_of_origin = models.CharField(null=False, blank=False, max_length=40, default=None)
    town_of_origin = models.CharField(null=False, blank=False, max_length=40, default=None)
    local_government_of_origin = models.CharField(null=False, blank=False, max_length=40, default=None)


    state_of_residence = models.CharField(null=False, blank=False, max_length=40, default=None)
    town_of_residence = models.CharField(null=False, blank=False, max_length=40, default=None)
    local_government_of_residence = models.CharField(null=False, blank=False, max_length=40, default=None)

    current_home_address = models.CharField(null=False, blank=False, max_length=200, default=None)
    current_office_address = models.CharField(null=False, blank=False, max_length=200, default=None)

    profession = models.CharField(null=False, blank=False, max_length=40, default=None)
    date_of_birth = models.DateField(null=False, blank=False, default=timezone.now)




# PRIVATE ORGANIZATION OWNER MODEL
class Doormot_User_Private_Organization_Owner(AbstractBaseUser, PermissionsMixin):

    
    ORGANIZATION_TYPE_CHOICES = [
        ('F', 'For Profit'),
        ('N', 'Non-Profit'),
        ('U', 'Prefer not to say'),
    ]

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name = 'user permissions',
        blank = True,
        related_name = 'Doormot_User_Private_Organization_Owner_Perm',
    )

    groups = models.ManyToManyField(
        Group, 
        verbose_name='groups', 
        blank=True, 
        related_name='private_org_owner_groups'
    )
    to_let_listings = GenericRelation('doormot_property_listing.To_Let_Listed_Properties')
    for_sale_listings = GenericRelation('doormot_property_listing.For_Sale_Listed_Properties')

    user_id = models.CharField(max_length=50, unique=True, default=None)
    false_log_count = models.PositiveIntegerField(null=True, default=None)
    currently_logged_in = models.BooleanField(null=True, default=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            current_date = timezone.now().date()
            random = rand()
            random_alphanumeric = random.alphanumeric()
            random_int = random.generate_random_number()

            self.user_id = f"PRV/ORG/OWN/{random_int}/{random_alphanumeric}/{current_date}"
        super().save(*args, **kwargs)


    organization_type = models.CharField(null=False, blank=False, max_length=40, choices=ORGANIZATION_TYPE_CHOICES,  default=None)

    official_registered_name = models.CharField(max_length=100, null=False, blank=False, unique=True, default=None)
    website = models.CharField(max_length=50, null=True, blank=True, unique=True, default=None)
    official_registered_number = models.CharField(max_length=50, null=False, blank=False, unique=True, default=None)
    office_address = models.CharField(max_length=150, null=False, blank=False, default=None)

    certificate_image = models.ImageField(upload_to='private_organization_tenant_certificate_images/',  default=None)

    username = models.CharField(max_length=30, unique=True, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=False, blank=False, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'

    class Meta:
        app_label = 'doormot_reg_users'

    def __str__(self):
        return self.username







































# SECTION: BUYERS
# Buyers models: Individual, Private Organization and Government


# INDIVIDUAL BUYER MODEL
class Doormot_User_Individual_Buyer_Details(models.Model):
 
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
        ('U', 'Prefer not to say'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('S', 'Single'),
        ('M', 'Married'),
        ('E', 'Engaged'),
        ('D', 'Divorced'),
        ('W', 'Widowed'),
        ('U', 'Prefer not to say'),
    ]

    EDUCATION_LEVEL_CHOICES = [
        ('H', 'High School Graduate'),
        ('G', 'University Graduate'),
        ('U', 'Undergraduate'),
        ('A', 'Apprenticeship Graduate'),
        ('U', 'Prefer not to say'),
    ]

    EMPLOYMENT_STATUS_CHOICES = [
        ('E', 'Employed'),
        ('U', 'Unemployed'),
        ('S', 'Self Employed'),
        ('U', 'Prefer not to say'),
    ]

    gender = models.CharField(null=False, blank=False, max_length=40, choices=GENDER_CHOICES,  default=None)
    education_level = models.CharField(null=False, blank=False, max_length=40, choices=EDUCATION_LEVEL_CHOICES,  default=None)
    marital_status = models.CharField(null=False, blank=False, max_length=40, choices=MARITAL_STATUS_CHOICES,  default=None)
    employment_status = models.CharField(null=False, blank=False, max_length=40, choices=EMPLOYMENT_STATUS_CHOICES, default=None)


    image = models.ImageField(upload_to='individual_owner_images/',  default=None)
    video = models.FileField(upload_to='individual_owner_videos/', validators=[validate_video_size], default=None)

    first_name = models.CharField(null=False, blank=False, max_length=40, default=None)
    middle_name = models.CharField(null=True, blank=True, max_length=40, default=None)
    last_name = models.CharField(null=False, blank=False, max_length=40, default=None)

    state_of_origin = models.CharField(null=False, blank=False, max_length=40, default=None)
    town_of_origin = models.CharField(null=False, blank=False, max_length=40, default=None)
    local_government_of_origin = models.CharField(null=False, blank=False, max_length=40, default=None)
    origin_home_address = models.CharField(null=False, blank=False, max_length=200, default=None)

    state_of_residence = models.CharField(null=False, blank=False, max_length=40, default=None)
    town_of_residence = models.CharField(null=False, blank=False, max_length=40, default=None)
    local_government_of_residence = models.CharField(null=False, blank=False, max_length=40, default=None)
    current_home_address = models.CharField(null=False, blank=False, max_length=200, default=None)

    date_of_birth = models.DateField(null=False, blank=False, default=timezone.now)
    


class Doormot_User_Individual_Buyer(AbstractBaseUser, PermissionsMixin):
    individual_tenant_details = models.OneToOneField(Doormot_User_Individual_Buyer_Details, on_delete=models.CASCADE, null=True, blank=True)

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name = 'user permissions',
        blank = True,
        related_name = 'Doormot_User_Individual_Buyer_Perm',
    )

    groups = models.ManyToManyField(
        Group, 
        verbose_name='groups', 
        blank=True, 
        related_name='individual_buyer_groups'
    )

    user_id = models.CharField(max_length=50, unique=True, default=None)
    false_log_count = models.PositiveIntegerField(null=True, default=None)
    currently_logged_in = models.BooleanField(null=True, default=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            current_date = timezone.now().date()
            random = rand()
            random_alphanumeric = random.alphanumeric()
            random_int = random.generate_random_number()

            self.user_id = f"IND/BYR/{random_int}/{random_alphanumeric}/{current_date}"
        super().save(*args, **kwargs)

    username = models.CharField(max_length=30, unique=True, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=False, blank=False, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'

    class Meta:
        app_label = 'doormot_reg_users'

    def __str__(self):
        return self.username


class Doormot_User_Individual_Buyer_Next_Of_Kin(models.Model):
    
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
        ('U', 'Prefer not to say'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('S', 'Single'),
        ('M', 'Married'),
        ('E', 'Engaged'),
        ('D', 'Divorced'),
        ('W', 'Widowed'),
        ('U', 'Prefer not to say'),
    ]

    EDUCATION_LEVEL_CHOICES = [
        ('H', 'High School Graduate'),
        ('G', 'University Graduate'),
        ('U', 'Undergraduate'),
        ('A', 'Apprenticeship Graduate'),
        ('U', 'Prefer not to say'),
    ]

    EMPLOYMENT_STATUS_CHOICES = [
        ('E', 'Employed'),
        ('U', 'Unemployed'),
        ('S', 'Self Employed'),
        ('U', 'Prefer not to say'),
    ]

    gender = models.CharField(null=False, blank=False, max_length=40, choices=GENDER_CHOICES,  default=None)
    education_level = models.CharField(null=False, blank=False, max_length=40, choices=EDUCATION_LEVEL_CHOICES,  default=None)
    marital_status = models.CharField(null=False, blank=False, max_length=40, choices=MARITAL_STATUS_CHOICES,  default=None)
    employment_status = models.CharField(null=False, blank=False, max_length=40, choices=EMPLOYMENT_STATUS_CHOICES, default=None)


    user = models.ForeignKey(Doormot_User_Individual_Buyer, on_delete=models.CASCADE, related_name='individual_Buyer_next_of_kin')
    
    email = models.EmailField(unique=True, null=False, blank=False, default=None)
    phone_number = models.CharField(unique=True, null=False, blank=False, max_length=15, default=None)

    image = models.ImageField(upload_to='individual_buyer_next_of_kin_images/', default=None)

    first_name = models.CharField(null=False, blank=False, max_length=40, default=None)
    middle_name = models.CharField(null=True, blank=True, max_length=40, default=None)
    last_name = models.CharField(null=False, blank=False, max_length=40, default=None)

    state_of_origin = models.CharField(null=False, blank=False, max_length=40, default=None)
    town_of_origin = models.CharField(null=False, blank=False, max_length=40, default=None)
    local_government_of_origin = models.CharField(null=False, blank=False, max_length=40, default=None)


    state_of_residence = models.CharField(null=False, blank=False, max_length=40, default=None)
    town_of_residence = models.CharField(null=False, blank=False, max_length=40, default=None)
    local_government_of_residence = models.CharField(null=False, blank=False, max_length=40, default=None)

    current_home_address = models.CharField(null=False, blank=False, max_length=200, default=None)
    current_office_address = models.CharField(null=False, blank=False, max_length=200, default=None)

    profession = models.CharField(null=False, blank=False, max_length=40, default=None)
    date_of_birth = models.DateField(null=False, blank=False, default=timezone.now)




# PRIVATE ORGANIZATION OWNER MODEL
class Doormot_User_Private_Organization_Buyer(AbstractBaseUser, PermissionsMixin):

    
    ORGANIZATION_TYPE_CHOICES = [
        ('F', 'For Profit'),
        ('N', 'Non-Profit'),
        ('U', 'Prefer not to say'),
    ]

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name = 'user permissions',
        blank = True,
        related_name = 'Doormot_User_Private_Organization_Buyer_Perm',
    )

    groups = models.ManyToManyField(
        Group, 
        verbose_name='groups', 
        blank=True, 
        related_name='private_org_buyer_groups'
    )

    user_id = models.CharField(max_length=50, unique=True, default=None)
    false_log_count = models.PositiveIntegerField(null=True, default=None)
    currently_logged_in = models.BooleanField(null=True, default=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            current_date = timezone.now().date()
            random = rand()
            random_alphanumeric = random.alphanumeric()
            random_int = random.generate_random_number()

            self.user_id = f"PRV/ORG/BYR/{random_int}/{random_alphanumeric}/{current_date}"
        super().save(*args, **kwargs)

    organization_type = models.CharField(null=False, blank=False, max_length=40, choices=ORGANIZATION_TYPE_CHOICES,  default=None)

    official_registered_name = models.CharField(max_length=100, null=False, blank=False, unique=True, default=None)
    website = models.CharField(max_length=50, null=True, blank=True, unique=True, default=None)
    official_registered_number = models.CharField(max_length=50, null=False, blank=False, unique=True, default=None)
    office_address = models.CharField(max_length=150, null=False, blank=False, default=None)

    certificate_image = models.ImageField(upload_to='private_organization_buyer_certificate_images/',  default=None)

    username = models.CharField(max_length=30, unique=True, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=False, blank=False, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'

    class Meta:
        app_label = 'doormot_reg_users'

    def __str__(self):
        return self.username





































# SECTION: TENANTS
# Agents models: Individual, Private Organization and Government

# INDIVIDUAL AGENT MODEL

class Doormot_User_Individual_Tenant_Details(models.Model):
 
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
        ('U', 'Prefer not to say'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('S', 'Single'),
        ('M', 'Married'),
        ('E', 'Engaged'),
        ('D', 'Divorced'),
        ('W', 'Widowed'),
        ('U', 'Prefer not to say'),
    ]

    EDUCATION_LEVEL_CHOICES = [
        ('H', 'High School Graduate'),
        ('G', 'University Graduate'),
        ('U', 'Undergraduate'),
        ('A', 'Apprenticeship Graduate'),
        ('U', 'Prefer not to say'),
    ]

    EMPLOYMENT_STATUS_CHOICES = [
        ('E', 'Employed'),
        ('U', 'Unemployed'),
        ('S', 'Self Employed'),
        ('U', 'Prefer not to say'),
    ]

    gender = models.CharField(null=False, blank=False, max_length=40, choices=GENDER_CHOICES,  default=None)
    education_level = models.CharField(null=False, blank=False, max_length=40, choices=EDUCATION_LEVEL_CHOICES,  default=None)
    marital_status = models.CharField(null=False, blank=False, max_length=40, choices=MARITAL_STATUS_CHOICES,  default=None)
    employment_status = models.CharField(null=False, blank=False, max_length=40, choices=EMPLOYMENT_STATUS_CHOICES, default=None)


    image = models.ImageField(upload_to='individual_tenant_images/',  default=None)
    video = models.FileField(upload_to='individual_tenant_videos/', validators=[validate_video_size], default=None)

    first_name = models.CharField(null=False, blank=False, max_length=40, default=None)
    middle_name = models.CharField(null=True, blank=True, max_length=40, default=None)
    last_name = models.CharField(null=False, blank=False, max_length=40, default=None)

    state_of_origin = models.CharField(null=False, blank=False, max_length=40, default=None)
    town_of_origin = models.CharField(null=False, blank=False, max_length=40, default=None)
    local_government_of_origin = models.CharField(null=False, blank=False, max_length=40, default=None)
    origin_home_address = models.CharField(null=False, blank=False, max_length=200, default=None)

    state_of_residence = models.CharField(null=False, blank=False, max_length=40, default=None)
    town_of_residence = models.CharField(null=False, blank=False, max_length=40, default=None)
    local_government_of_residence = models.CharField(null=False, blank=False, max_length=40, default=None)
    current_home_address = models.CharField(null=False, blank=False, max_length=200, default=None)

    date_of_birth = models.DateField(null=False, blank=False, default=timezone.now)
    

class Doormot_User_Individual_Tenant(AbstractBaseUser, PermissionsMixin):
    individual_tenant_details = models.OneToOneField(Doormot_User_Individual_Tenant_Details, on_delete=models.CASCADE, null=True, blank=True)

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name = 'user permissions',
        blank = True,
        related_name = 'Doormot_User_Individual_Tenant_Perm',
    )

    groups = models.ManyToManyField(
        Group, 
        verbose_name='groups', 
        blank=True, 
        related_name='individual_tenant_groups'
    )

    user_id = models.CharField(max_length=50, unique=True, default=None)
    false_log_count = models.PositiveIntegerField(null=True, default=None)
    currently_logged_in = models.BooleanField(null=True, default=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            current_date = timezone.now().date()
            random = rand()
            random_alphanumeric = random.alphanumeric()
            random_int = random.generate_random_number()

            self.user_id = f"IND/TNT/{random_int}/{random_alphanumeric}/{current_date}"
        super().save(*args, **kwargs)

    username = models.CharField(max_length=30, unique=True, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=False, blank=False, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'

    class Meta:
        app_label = 'doormot_reg_users'

    def __str__(self):
        return self.username


class Doormot_User_Individual_Tenant_Next_Of_Kin(models.Model):
    
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
        ('U', 'Prefer not to say'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('S', 'Single'),
        ('M', 'Married'),
        ('E', 'Engaged'),
        ('D', 'Divorced'),
        ('W', 'Widowed'),
        ('U', 'Prefer not to say'),
    ]

    EDUCATION_LEVEL_CHOICES = [
        ('H', 'High School Graduate'),
        ('G', 'University Graduate'),
        ('U', 'Undergraduate'),
        ('A', 'Apprenticeship Graduate'),
        ('U', 'Prefer not to say'),
    ]

    EMPLOYMENT_STATUS_CHOICES = [
        ('E', 'Employed'),
        ('U', 'Unemployed'),
        ('S', 'Self Employed'),
        ('U', 'Prefer not to say'),
    ]

    gender = models.CharField(null=False, blank=False, max_length=40, choices=GENDER_CHOICES,  default=None)
    education_level = models.CharField(null=False, blank=False, max_length=40, choices=EDUCATION_LEVEL_CHOICES,  default=None)
    marital_status = models.CharField(null=False, blank=False, max_length=40, choices=MARITAL_STATUS_CHOICES,  default=None)
    employment_status = models.CharField(null=False, blank=False, max_length=40, choices=EMPLOYMENT_STATUS_CHOICES, default=None)


    user = models.ForeignKey(Doormot_User_Individual_Tenant, on_delete=models.CASCADE, related_name='individual_tenant_next_of_kin')
    
    email = models.EmailField(unique=True, null=False, blank=False, default=None)
    phone_number = models.CharField(unique=True, null=False, blank=False, max_length=15, default=None)

    image = models.ImageField(upload_to='individual_tenant_next_of_kin_images/', default=None)

    first_name = models.CharField(null=False, blank=False, max_length=40, default=None)
    middle_name = models.CharField(null=True, blank=True, max_length=40, default=None)
    last_name = models.CharField(null=False, blank=False, max_length=40, default=None)

    state_of_origin = models.CharField(null=False, blank=False, max_length=40, default=None)
    town_of_origin = models.CharField(null=False, blank=False, max_length=40, default=None)
    local_government_of_origin = models.CharField(null=False, blank=False, max_length=40, default=None)


    state_of_residence = models.CharField(null=False, blank=False, max_length=40, default=None)
    town_of_residence = models.CharField(null=False, blank=False, max_length=40, default=None)
    local_government_of_residence = models.CharField(null=False, blank=False, max_length=40, default=None)

    current_home_address = models.CharField(null=False, blank=False, max_length=200, default=None)
    current_office_address = models.CharField(null=False, blank=False, max_length=200, default=None)

    profession = models.CharField(null=False, blank=False, max_length=40, default=None)
    date_of_birth = models.DateField(null=False, blank=False, default=timezone.now)




# PRIVATE ORGANIZATION TENANT MODEL
class Doormot_User_Private_Organization_Tenant(AbstractBaseUser, PermissionsMixin):

    
    ORGANIZATION_TYPE_CHOICES = [
        ('F', 'For Profit'),
        ('N', 'Non-Profit'),
        ('U', 'Prefer not to say'),
    ]

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name = 'user permissions',
        blank = True,
        related_name = 'Doormot_User_Private_Organization_Tenant_Perm',
    )

    groups = models.ManyToManyField(
        Group, 
        verbose_name='groups', 
        blank=True, 
        related_name='private_org_tenant_groups'
    )

    user_id = models.CharField(max_length=50, unique=True, default=None)
    false_log_count = models.PositiveIntegerField(null=True, default=None)
    currently_logged_in = models.BooleanField(null=True, default=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            current_date = timezone.now().date()
            random = rand()
            random_alphanumeric = random.alphanumeric()
            random_int = random.generate_random_number()

            self.user_id = f"PRV/ORG/TNT/{random_int}/{random_alphanumeric}/{current_date}"
        super().save(*args, **kwargs)

    organization_type = models.CharField(null=False, blank=False, max_length=40, choices=ORGANIZATION_TYPE_CHOICES,  default=None)

    official_registered_name = models.CharField(max_length=100, null=False, blank=False, unique=True, default=None)
    website = models.CharField(max_length=50, null=True, blank=True, unique=True, default=None)
    official_registered_number = models.CharField(max_length=50, null=False, blank=False, unique=True, default=None)
    office_address = models.CharField(max_length=150, null=False, blank=False, default=None)

    certificate_image = models.ImageField(upload_to='private_organization_tenant_certificate_images/',  default=None)

    username = models.CharField(max_length=30, unique=True, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=False, blank=False, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'

    class Meta:
        app_label = 'doormot_reg_users'

    def __str__(self):
        return self.username
















































# SECTION: AGENTS
# Agents models: Official and Independent

# OFFICIAL AGENT MODEL

class Doormot_User_Official_Agent_Details(models.Model):
 
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
        ('U', 'Prefer not to say'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('S', 'Single'),
        ('M', 'Married'),
        ('E', 'Engaged'),
        ('D', 'Divorced'),
        ('W', 'Widowed'),
        ('U', 'Prefer not to say'),
    ]

    EDUCATION_LEVEL_CHOICES = [
        ('H', 'High School Graduate'),
        ('G', 'University Graduate'),
        ('U', 'Undergraduate'),
        ('A', 'Apprenticeship Graduate'),
        ('U', 'Prefer not to say'),
    ]

    EMPLOYMENT_STATUS_CHOICES = [
        ('E', 'Employed'),
        ('U', 'Unemployed'),
        ('S', 'Self Employed'),
        ('U', 'Prefer not to say'),
    ]

    gender = models.CharField(null=False, blank=False, max_length=40, choices=GENDER_CHOICES,  default=None)
    education_level = models.CharField(null=False, blank=False, max_length=40, choices=EDUCATION_LEVEL_CHOICES,  default=None)
    marital_status = models.CharField(null=False, blank=False, max_length=40, choices=MARITAL_STATUS_CHOICES,  default=None)
    employment_status = models.CharField(null=False, max_length=40, choices=EMPLOYMENT_STATUS_CHOICES, default=None)

    
    image = models.ImageField(upload_to='official_agent_images/',  default=None)
    video = models.FileField(upload_to='official_agent_videos/', validators=[validate_video_size], default=None)

    first_name = models.CharField(null=False, blank=False, max_length=40, default=None)
    middle_name = models.CharField(null=True, blank=True, max_length=40, default=None)
    last_name = models.CharField(null=False, blank=False, max_length=40, default=None)

    state_of_origin = models.CharField(null=False, blank=False, max_length=40, default=None)
    town_of_origin = models.CharField(null=False, blank=False, max_length=40, default=None)
    local_government_of_origin = models.CharField(null=False, blank=False, max_length=40, default=None)
    origin_home_address = models.CharField(null=False, blank=False, max_length=200, default=None)

    state_of_residence = models.CharField(null=False, blank=False, max_length=40, default=None)
    town_of_residence = models.CharField(null=False, blank=False, max_length=40, default=None)
    local_government_of_residence = models.CharField(null=False, blank=False, max_length=40, default=None)
    current_home_address = models.CharField(null=False, blank=False, max_length=200, default=None)


class Doormot_User_Official_Agent(AbstractBaseUser, PermissionsMixin):

    official_agent_details = models.OneToOneField(Doormot_User_Official_Agent_Details, on_delete=models.CASCADE, null=True, blank=True)

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name = 'user permissions',
        blank = True,
        related_name = 'Doormot_User_Official_Agent_Perm',
    )

    groups = models.ManyToManyField(
        Group, 
        verbose_name='groups', 
        blank=True, 
        related_name='official_agent_groups'
    )

    to_let_listings = GenericRelation('doormot_property_listing.To_Let_Listed_Properties')
    for_sale_listings = GenericRelation('doormot_property_listing.For_Sale_Listed_Properties')
    
    agent_id = models.CharField(max_length=50, unique=True, default=None)
    false_log_count = models.PositiveIntegerField(null=True, default=None)
    date_of_birth = models.DateField(null=False, blank=False, default=timezone.now)
    currently_logged_in = models.BooleanField(null=True, default=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            current_date = timezone.now().date()
            random = rand()
            random_alphanumeric = random.alphanumeric()
            random_int = random.generate_random_number()

            self.agent_id = f"OFCL/AGNT/{random_int}/{random_alphanumeric}/{current_date}"
        super().save(*args, **kwargs)

    username = models.CharField(max_length=30, unique=True, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=False, blank=False, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'

    class Meta:
        app_label = 'doormot_reg_users'

    def __str__(self):
        return self.username    


class Doormot_User_Official_Agent_Next_Of_Kin(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
        ('U', 'Prefer not to say'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('S', 'Single'),
        ('M', 'Married'),
        ('E', 'Engaged'),
        ('D', 'Divorced'),
        ('W', 'Widowed'),
        ('U', 'Prefer not to say'),
    ]

    EDUCATION_LEVEL_CHOICES = [
        ('H', 'High School Graduate'),
        ('G', 'University Graduate'),
        ('U', 'Undergraduate'),
        ('A', 'Apprenticeship Graduate'),
        ('U', 'Prefer not to say'),
    ]

    EMPLOYMENT_STATUS_CHOICES = [
        ('E', 'Employed'),
        ('U', 'Unemployed'),
        ('S', 'Self Employed'),
        ('U', 'Prefer not to say'),
    ]

    gender = models.CharField(null=False, blank=False, max_length=40, choices=GENDER_CHOICES,  default=None)
    education_level = models.CharField(null=False, blank=False, max_length=40, choices=EDUCATION_LEVEL_CHOICES,  default=None)
    marital_status = models.CharField(null=False, blank=False, max_length=40, choices=MARITAL_STATUS_CHOICES,  default=None)
    employment_status = models.CharField(null=False, max_length=40, choices=EMPLOYMENT_STATUS_CHOICES, default=None)


    user = models.ForeignKey(Doormot_User_Official_Agent, on_delete=models.CASCADE, related_name='official_agent_next_of_kin')
    
    email = models.EmailField(unique=True, null=False, blank=False, default=None)
    phone_number = models.CharField(unique=True, null=False, blank=False, max_length=15, default=None)

    image = models.ImageField(upload_to='official_agent_next_of_kin_images/', default=None)

    first_name = models.CharField(null=False, blank=False, max_length=40, default=None)
    middle_name = models.CharField(null=True, blank=True, max_length=40, default=None)
    last_name = models.CharField(null=False, blank=False, max_length=40, default=None)

    state_of_origin = models.CharField(null=False, blank=False, max_length=40, default=None)
    town_of_origin = models.CharField(null=False, blank=False, max_length=40, default=None)
    local_government_of_origin = models.CharField(null=False, blank=False, max_length=40, default=None)


    state_of_residence = models.CharField(null=False, blank=False, max_length=40, default=None)
    town_of_residence = models.CharField(null=False, blank=False, max_length=40, default=None)
    local_government_of_residence = models.CharField(null=False, blank=False, max_length=40, default=None)

    current_home_address = models.CharField(null=False, blank=False, max_length=200, default=None)
    current_office_address = models.CharField(null=False, blank=False, max_length=200, default=None)

    profession = models.CharField(null=False, blank=False, max_length=40, default=None)
    date_of_birth = models.DateField(null=False, blank=False, default=timezone.now)


class Doormot_User_Official_Agent_Guarantor(models.Model):
        
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
        ('U', 'Prefer not to say'),
    ]
    
    user = models.ForeignKey(Doormot_User_Official_Agent, on_delete=models.CASCADE, related_name='official_agent_guarantor')
    
    email = models.EmailField(unique=True, null=False, blank=False, default=None)
    phone_number = models.CharField(unique=True, null=False, blank=False, max_length=15, default=None)

    image = models.ImageField(upload_to='official_agent_next_of_kin_images/', default=None)

    first_name = models.CharField(null=False, blank=False, max_length=40, default=None)
    middle_name = models.CharField(null=False, blank=False, max_length=40, default=None)
    last_name = models.CharField(null=False, blank=False, max_length=40, default=None)
    gender = models.CharField(null=False, blank=False, max_length=1, choices=GENDER_CHOICES, default=None)

    state_of_origin = models.CharField(null=False, blank=False, max_length=40, default=None)
    town_of_origin = models.CharField(null=False, blank=False, max_length=40, default=None)
    local_government_of_origin = models.CharField(null=False, blank=False, max_length=40, default=None)


    state_of_residence = models.CharField(null=False, blank=False, max_length=40, default=None)
    town_of_residence = models.CharField(null=False, blank=False, max_length=40, default=None)
    local_government_of_residence = models.CharField(null=False, blank=False, max_length=40, default=None)

    current_home_address = models.CharField(null=False, blank=False, max_length=200, default=None)
    current_office_address = models.CharField(null=False, blank=False, max_length=200, default=None)

    profession = models.CharField(null=False, blank=False, max_length=40, default=None)
    date_of_birth = models.DateField(null=False, blank=False, default=timezone.now)


































# INDEPENDENT AGENT MODEL
class Doormot_User_Independent_Agent_Details(models.Model):
 
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
        ('U', 'Prefer not to say'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('S', 'Single'),
        ('M', 'Married'),
        ('E', 'Engaged'),
        ('D', 'Divorced'),
        ('W', 'Widowed'),
        ('U', 'Prefer not to say'),
    ]

    EDUCATION_LEVEL_CHOICES = [
        ('H', 'High School Graduate'),
        ('G', 'University Graduate'),
        ('U', 'Undergraduate'),
        ('A', 'Apprenticeship Graduate'),
        ('U', 'Prefer not to say'),
    ]

    EMPLOYMENT_STATUS_CHOICES = [
        ('E', 'Employed'),
        ('U', 'Unemployed'),
        ('S', 'Self Employed'),
        ('U', 'Prefer not to say'),
    ]

    gender = models.CharField(null=True, blank=True, max_length=40, choices=GENDER_CHOICES,  default=None)
    education_level = models.CharField(null=True, blank=True, max_length=40, choices=EDUCATION_LEVEL_CHOICES,  default=None)
    marital_status = models.CharField(null=True, blank=True, max_length=40, choices=MARITAL_STATUS_CHOICES,  default=None)
    employment_status = models.CharField(null=False, max_length=40, choices=EMPLOYMENT_STATUS_CHOICES, default=None)

    image = models.ImageField(upload_to='independent_agent_images/',  default=None)
    video = models.FileField(upload_to='independent_agent_videos/', validators=[validate_video_size], default=None)

    first_name = models.CharField(null=True, blank=True, max_length=40, default=None)
    middle_name = models.CharField(null=True, blank=True, max_length=40, default=None)
    last_name = models.CharField(null=True, blank=True, max_length=40, default=None)
    

    state_of_origin = models.CharField(null=True, blank=True, max_length=40, default=None)
    town_of_origin = models.CharField(null=True, blank=True, max_length=40, default=None)
    local_government_of_origin = models.CharField(null=True, blank=True, max_length=40, default=None)
    origin_home_address = models.CharField(null=True, blank=True, max_length=200, default=None)

    state_of_residence = models.CharField(null=True, blank=True, max_length=40, default=None)
    town_of_residence = models.CharField(null=True, blank=True, max_length=40, default=None)
    local_government_of_residence = models.CharField(null=True, blank=True, max_length=40, default=None)
    current_home_address = models.CharField(null=True, blank=True, max_length=200, default=None)


class Doormot_User_Independent_Agent(AbstractBaseUser):

    independent_agent_details = models.OneToOneField(Doormot_User_Independent_Agent_Details, on_delete=models.CASCADE, null=True, blank=True)

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name = 'user permissions',
        blank = True,
        related_name = 'Doormot_User_Independent_Agent_Perm',
    )

    groups = models.ManyToManyField(
        Group, 
        verbose_name='groups', 
        blank=True, 
        related_name='indipendent_agent_groups'
    )

    to_let_listings = GenericRelation('doormot_property_listing.To_Let_Listed_Properties')
    for_sale_listings = GenericRelation('doormot_property_listing.For_Sale_Listed_Properties')

    agent_id = models.CharField(max_length=50, unique=True, default=None)
    false_log_count = models.PositiveIntegerField(null=True, default=None)
    date_of_birth = models.DateField(null=False, blank=False, default=timezone.now)
    currently_logged_in = models.BooleanField(null=True, default=False)


    def save(self, *args, **kwargs):
        if not self.pk:
            current_date = timezone.now().date()
            random = rand()
            random_alphanumeric = random.alphanumeric()
            random_int = random.generate_random_number()

            self.agent_id = f"INDP/AGNT/{random_int}/{random_alphanumeric}/{current_date}"
        super().save(*args, **kwargs)
    
    username = models.CharField(max_length=30, unique=True, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=False, blank=False, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'

    class Meta:
        app_label = 'doormot_reg_users'

    def __str__(self):
        return self.username


class Doormot_User_Independent_Agent_Next_Of_Kin(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
        ('U', 'Prefer not to say'),
    ]

    user = models.ForeignKey(Doormot_User_Independent_Agent, on_delete=models.CASCADE, related_name='independent_agent_next_of_kin')
    
    email = models.EmailField(unique=True, null=True, blank=True, default=None)
    phone_number = models.CharField(unique=True, null=True, blank=True, max_length=15, default=None)

    image = models.ImageField(upload_to='independent_agent_next_of_kin_images/', default=None)

    first_name = models.CharField(null=True, blank=True, max_length=40, default=None)
    middle_name = models.CharField(null=True, blank=True, max_length=40, default=None)
    last_name = models.CharField(null=True, blank=True, max_length=40, default=None)
    gender = models.CharField(null=True, blank=True, max_length=1, choices=GENDER_CHOICES, default=None)

    state_of_origin = models.CharField(null=True, blank=True, max_length=40, default=None)
    town_of_origin = models.CharField(null=True, blank=True, max_length=40, default=None)
    local_government_of_origin = models.CharField(null=True, blank=True, max_length=40, default=None)


    state_of_residence = models.CharField(null=True, blank=True, max_length=40, default=None)
    town_of_residence = models.CharField(null=True, blank=True, max_length=40, default=None)
    local_government_of_residence = models.CharField(null=True, blank=True, max_length=40, default=None)

    current_home_address = models.CharField(null=True, blank=True, max_length=200, default=None)
    current_office_address = models.CharField(null=True, blank=True, max_length=200, default=None)

    profession = models.CharField(null=True, blank=True, max_length=40, default=None)
    date_of_birth = models.DateField(null=True, blank=True, default=timezone.now)


class Doormot_User_Independent_Agent_Guarantor(models.Model):
        
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
        ('U', 'Prefer not to say'),
    ]
    
    user = models.ForeignKey(Doormot_User_Independent_Agent, on_delete=models.CASCADE, related_name='independent_agent_guarantor')
    
    email = models.EmailField(unique=True, null=True, blank=True, default=None)
    phone_number = models.CharField(unique=True, null=True, blank=True, max_length=15, default=None)

    image = models.ImageField(upload_to='independent_agent_next_of_kin_images/', default=None)

    first_name = models.CharField(null=True, blank=True, max_length=40, default=None)
    middle_name = models.CharField(null=True, blank=True, max_length=40, default=None)
    last_name = models.CharField(null=True, blank=True, max_length=40, default=None)
    gender = models.CharField(null=True, blank=True, max_length=1, choices=GENDER_CHOICES, default=None)

    state_of_origin = models.CharField(null=True, blank=True, max_length=40, default=None)
    town_of_origin = models.CharField(null=True, blank=True, max_length=40, default=None)
    local_government_of_origin = models.CharField(null=True, blank=True, max_length=40, default=None)


    state_of_residence = models.CharField(null=True, blank=True, max_length=40, default=None)
    town_of_residence = models.CharField(null=True, blank=True, max_length=40, default=None)
    local_government_of_residence = models.CharField(null=True, blank=True, max_length=40, default=None)

    current_home_address = models.CharField(null=True, blank=True, max_length=200, default=None)
    current_office_address = models.CharField(null=True, blank=True, max_length=200, default=None)

    profession = models.CharField(null=True, blank=True, max_length=40, default=None)
    date_of_birth = models.DateField(null=True, blank=True, default=timezone.now)