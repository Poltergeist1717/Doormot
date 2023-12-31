from django.db import models
from django.contrib.auth import validators
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from doormot_reg_users.doormot_reg_modules import rand
from django.contrib.contenttypes.fields import GenericRelation




def validate_video_size(value):
    # Specify the maximum file size (e.g., 10MB)
    max_size = 10 * 1024 * 1024  # 10MB in bytes

    if value.size > max_size:
        raise ValidationError('File size cannot exceed 10MB.')


class For_Sale_Listed_Properties(models.Model):

    uploaded_by = GenericForeignKey('uploaded_by_content_type', 'uploaded_by_object_id')
    uploaded_by_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    uploaded_by_object_id = models.PositiveIntegerField()

    uploader_user_type = models.CharField(max_length=50, blank=False, null=False, default=None)
    
    reverse_relation_individual_owner = GenericRelation('doormot_reg_users.Doormot_User_Individual_Owner')
    reverse_relation_private_organization_owner = GenericRelation('doormot_reg_users.Doormot_User_Private_Organization_Owner') 
    reverse_relation_official_agent = GenericRelation('doormot_reg_users.Doormot_User_Official_Agent')
    reverse_relation_independent_agent = GenericRelation('doormot_reg_users.Doormot_User_Independent_Agent')

    title = models.CharField(max_length=100)
    closest_landmark = models.CharField(max_length=100, blank=False, null=False, default=None)
    description = models.TextField(blank=False, null=False, default=None)

    property_id = models.CharField(max_length=50, unique=True, default=None)

    owned_by = models.CharField(max_length=50, blank=False, null=False, default=None)

    asking_price = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False, default=None)
    property_status = models.CharField(max_length=50, blank=False, null=False, default=None)
    property_type = models.CharField(max_length=50, blank=False, null=False, default=None)

    sub_commercial_property_type = models.CharField(max_length=50, blank=True, null=True, default=None)
    
    sub_school_type = models.CharField(max_length=50, blank=True, null=True, default=None)
    no_of_classrooms = models.PositiveIntegerField(blank=False, null=False, default=None)
    student_enrollment_trend = models.TextField(blank=False, null=False, default=None)
    academic_performance_and_accreditation_status = models.TextField(blank=False, null=False, default=None)  

    sub_medical_building_type = models.CharField(max_length=50, blank=True, null=True, default=None)
    no_of_patient_bedspace = models.PositiveIntegerField(blank=False, null=False, default=None)
    current_patient_capacity = models.PositiveIntegerField(blank=False, null=False, default=None)
    medical_services_demand = models.CharField(max_length=50, blank=False, null=False, default=None)
    medical_services_demand_more_info = models.TextField(blank=True, null=False, default=None)
    retain_existing_medical_staff = models.CharField(max_length=50, blank=False, null=False, default=None)
    retain_existing_medical_staff_more_info = models.TextField(blank=True, null=False, default=None)

    backup_power_system = models.CharField(max_length=50, blank=False, null=False, default=None)
    backup_power_system_more_info = models.TextField(blank=True, null=False, default=None)
    property_accessibility = models.CharField(max_length=50, blank=False, null=False, default=None)
    property_area_security_status = models.CharField(max_length=50, blank=False, null=False, default=None)
    religious_building_clsoeby = models.CharField(max_length=50, blank=False, null=False, default=None)
    religious_building_clsoeby_type = models.CharField(max_length=50, blank=False, null=False, default=None)
    restrictions_association_rules = models.CharField(max_length=50, blank=False, null=False, default=None)
    restrictions_association_rules_more_info = models.TextField(blank=False, null=False, default=None)
    outstanding_issues_and_repair = models.CharField(max_length=50, blank=False, null=False, default=None)
    outstanding_issues_and_repair_more_info = models.TextField(blank=True, null=False, default=None)
    property_recuurent_costs = models.CharField(max_length=50, blank=False, null=False, default=None)
    property_recuurent_costs_more_info = models.TextField(blank=True, null=False, default=None)
    property_area_internet_connectivity = models.CharField(max_length=50, blank=False, null=False, default=None)
      
    no_of_bedrooms = models.PositiveIntegerField(blank=False, null=False, default=None)
    no_of_livingrooms = models.PositiveIntegerField(blank=False, null=False, default=None)
    no_of_bathrooms = models.PositiveIntegerField(blank=False, null=False, default=None)
    no_of_kitchens = models.PositiveIntegerField(blank=False, null=False, default=None)
    size_of_property_by_square_footage = models.PositiveIntegerField(blank=False, null=False, default=None)
    size_of_property_by_plot = models.PositiveIntegerField(blank=False, null=False, default=None)

    address = models.CharField(max_length=255, blank=False, null=False, default=None)
    city = models.CharField(max_length=100, blank=False, null=False, default=None)
    state = models.CharField(max_length=100, blank=False, null=False, default=None)
    zip_code = models.PositiveIntegerField(blank=False, null=False, default=None)
    local_government = models.CharField(max_length=20, blank=False, null=False, default=None)

    available_amenities = models.ManyToManyField('self', blank=True)

    date_time_of_upload = models.DateTimeField(auto_now_add=True)
    year_developed = models.PositiveIntegerField(blank=False, null=False, default=None)

    date_time_of_sale = models.DateTimeField(null=True, default=None)

    is_negotiable = models.BooleanField(default=False)
    is_sold = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            random = rand()
            random_int = random.generate_random_number()
            random_alph = random.generate()
            random_int2 = random.generate_random_number()

            self.property_id = f"FSL-PPT/{random_int}/{random_alph}/{random_int2}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.get_property_type_display()}"

class For_Sale_Properties_Images(models.Model):
    connected_property = models.ForeignKey(For_Sale_Listed_Properties, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='property_images/', null=False, blank=False, default=None)



class To_Let_Listed_Properties(models.Model):

    uploaded_by = GenericForeignKey('uploaded_by_content_type', 'uploaded_by_object_id')
    uploaded_by_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    uploaded_by_object_id = models.PositiveIntegerField()

    uploader_user_type = models.CharField(max_length=50, blank=False, null=False, default=None)


    reverse_relation_individual_owner = GenericRelation('doormot_reg_users.Doormot_User_Individual_Owner')
    reverse_relation_private_organization_owner = GenericRelation('doormot_reg_users.Doormot_User_Private_Organization_Owner') 
    reverse_relation_official_agent = GenericRelation('doormot_reg_users.Doormot_User_Official_Agent')
    reverse_relation_independent_agent = GenericRelation('doormot_reg_users.Doormot_User_Independent_Agent')
    
    title = models.CharField(max_length=100)
    closest_landmark = models.CharField(max_length=50, blank=False, null=False, default=None)
    description = models.TextField(blank=False, null=False, default=None)

    property_id = models.CharField(max_length=50, unique=True, default=None)

    owned_by = models.CharField(max_length=50, blank=False, null=False, default=None)

    rent_price = models.DecimalField(max_digits=10, decimal_places=2)
    property_status = models.CharField(max_length=50)
    property_type = models.CharField(max_length=50)

    sub_commercial_property_type = models.CharField(max_length=50, blank=True, null=True, default=None)

    sub_school_type = models.CharField(max_length=50, blank=True, null=True, default=None)
    no_of_classrooms = models.PositiveIntegerField(blank=False, null=False, default=None)
    student_enrollment_trend = models.TextField(blank=False, null=False, default=None)
    academic_performance_and_accreditation_status = models.TextField(blank=False, null=False, default=None)  

    sub_medical_building_type = models.CharField(max_length=50, blank=True, null=True, default=None)
    no_of_patient_bedspace = models.PositiveIntegerField(blank=False, null=False, default=None)
    current_patient_capacity = models.PositiveIntegerField(blank=False, null=False, default=None)
    medical_services_demand = models.CharField(max_length=50, blank=False, null=False, default=None)
    medical_services_demand_more_info = models.TextField(blank=True, null=False, default=None)
    retain_existing_medical_staff = models.CharField(max_length=50, blank=False, null=False, default=None)
    retain_existing_medical_staff_more_info = models.TextField(blank=True, null=False, default=None)

    backup_power_system = models.CharField(max_length=50, blank=False, null=False, default=None)
    backup_power_system_more_info = models.TextField(blank=True, null=False, default=None)
    property_accessibility = models.CharField(max_length=50, blank=False, null=False, default=None)
    property_area_security_status = models.CharField(max_length=50, blank=False, null=False, default=None)
    religious_building_clsoeby = models.CharField(max_length=50, blank=False, null=False, default=None)
    religious_building_clsoeby_type = models.CharField(max_length=50, blank=False, null=False, default=None)
    restrictions_association_rules = models.CharField(max_length=50, blank=False, null=False, default=None)
    restrictions_association_rules_more_info = models.TextField(blank=False, null=False, default=None)
    outstanding_issues_and_repair = models.CharField(max_length=50, blank=False, null=False, default=None)
    outstanding_issues_and_repair_more_info = models.TextField(blank=True, null=False, default=None)
    property_recuurent_costs = models.CharField(max_length=50, blank=False, null=False, default=None)
    property_recuurent_costs_more_info = models.TextField(blank=True, null=False, default=None)
    property_area_internet_connectivity = models.CharField(max_length=50, blank=False, null=False, default=None)
    
    bathroom_is_available = models.CharField(max_length=50, blank=False, null=False, default=None)
    toilet_is_available = models.CharField(max_length=50, blank=False, null=False, default=None)
    water_is_available = models.CharField(max_length=50, blank=False, null=False, default=None)
    good_power_supply = models.CharField(max_length=50, blank=False, null=False, default=None)
    owner_lives_in_property = models.CharField(max_length=50, blank=False, null=False, default=None)

    address = models.CharField(max_length=255, blank=False, null=False, default=None)
    senatorial_district = models.CharField(max_length=100,blank=False, null=False, default=None)
    state = models.CharField(max_length=100, blank=False, null=False, default=None)
    zip_code = models.CharField(max_length=20)
    local_government = models.CharField(max_length=20, blank=False, null=False, default=None)

    available_amenities = models.ManyToManyField('self', blank=True)
    
    date_time_of_upload = models.DateTimeField(auto_now_add=True)
    year_developed = models.PositiveIntegerField(blank=False, null=False, default=None)

    is_rented = models.BooleanField(default=False)
    is_available_for_lease =  models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            random = rand()
            random_int = random.generate_random_number()
            random_alph = random.generate()
            random_int2 = random.generate_random_number()

            self.property_id = f"TLT-PPT/{random_int}/{random_alph}/{random_int2}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.get_property_type_display()}"


class To_Let_Properties_Images(models.Model):
    connected_property = models.ForeignKey(To_Let_Listed_Properties, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='property_images/', null=False, blank=False, default=None)
