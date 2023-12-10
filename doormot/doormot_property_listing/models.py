from django.db import models
from django.contrib.auth import validators
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from doormot_reg_users.doormot_reg_modules import rand



def validate_video_size(value):
    # Specify the maximum file size (e.g., 10MB)
    max_size = 10 * 1024 * 1024  # 10MB in bytes

    if value.size > max_size:
        raise ValidationError('File size cannot exceed 10MB.')


class For_Sale_Listed_Properties(models.Model):
    
    PROPERTY_STATUS = [
        ('N', 'New'),
        ('I', 'In use'),
        ('R', 'Renovated'),
        ('O', 'Old'),
        ]

    OWNED_BY_STATUS = [
        ('I', 'Individual'),
        ('C', 'Cooperate body'),
        ('G', 'Government'),
        ]

    PROPERTY_TYPES = [
        ('B', 'Bungalow'),
        ('D', 'Duplex'),
        ('DTH', 'Detached House'),
        ('TH', 'Terraced House'),
        ('BF', 'Block of Flats'),
        ('M', 'Mansion'),
        ('SC', 'Self-contained Apartment'),
        ('CB', 'Commercial Building'),
        ('RE', 'Residential Estate'),
        ]

    SUB_COMMERCIAL_PROPERTY_TYPES = [
        ('SHP', 'Shopping Complex'),
        ('OS', 'Office Space'),
        ('SSHPU', 'Shop Units'),
        ('SCHL', 'School Building'),
        ('HSPTL', 'Hospital Building'),
        ('PTRLSTN', 'Petrol Station'),
        ('RSTRNT', 'Restaurant Building'),
        ]


    uploaded_by = GenericForeignKey('uploaded_by_content_type', 'uploaded_by_object_id')
    uploaded_by_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    uploaded_by_object_id = models.PositiveIntegerField()

    title = models.CharField(max_length=100)
    closest_landmark = models.CharField(max_length=100, blank=False, null=False, default=None)
    description = models.TextField(blank=False, null=False, default=None)

    property_id = models.CharField(max_length=50, unique=True, default=None)

    owned_by = models.CharField(max_length=50, blank=False, null=False, default=None, choices=OWNED_BY_STATUS)

    asking_price = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False, default=None)
    property_status = models.CharField(max_length=50, blank=False, null=False, default=None, choices=PROPERTY_STATUS)
    property_type = models.CharField(max_length=50, blank=False, null=False, default=None, choices=PROPERTY_TYPES)
    sub_commercial_property_type = models.CharField(max_length=50, blank=False, null=False, default=None, choices=SUB_COMMERCIAL_PROPERTY_TYPES)
    no_of_bedrooms = models.PositiveIntegerField(blank=False, null=False, default=None)

    no_of_livingrooms = models.PositiveIntegerField(blank=False, null=False, default=None)
    no_of_bathrooms = models.PositiveIntegerField(blank=False, null=False, default=None)
    no_of_kitchens = models.PositiveIntegerField(blank=False, null=False, default=None)
    size_of_property_by_square_footage = models.PositiveIntegerField(blank=False, null=False, default=None)
    size_of_property_by_plot = models.PositiveIntegerField(blank=False, null=False, default=None)

    address = models.CharField(max_length=255, blank=False, null=False, default=None)
    city = models.CharField(max_length=100, blank=False, null=False, default=None)
    state = models.CharField(max_length=100, blank=False, null=False, default=None)
    zip_code = models.CharField(max_length=20, blank=True, null=True, default=None)
    local_government = models.CharField(max_length=20, blank=False, null=False, default=None)

    date_time_of_upload = models.DateTimeField(auto_now_add=True)
    year_developed = models.DateField(blank=False, null=False, default=None)

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
    
    PROPERTY_STATUS = [
        ('N', 'New'),
        ('R', 'Renovated'),
        ('O', 'Old'),
        ]

    OWNED_BY_STATUS = [
        ('I', 'Individual'),
        ('C', 'Cooperate body'),
        ('G', 'Government'),
        ]

    PROPERTY_TYPES = [
        ('B', 'Bungalow'),
        ('D', 'Duplex'),
        ('DT', 'Detached House'),
        ('T', 'Terraced House'),
        ('BF', 'Block of Flats'),
        ('M', 'Mansion'),
        ('SC', 'Self-contained Apartment'),
        ('CB', 'Commercial Building'),
        ('RE', 'Residential Estate'),
        ]

    SUB_COMMERCIAL_PROPERTY_TYPES = [
        ('SHP', 'Shopping Complex'),
        ('OS', 'Office Space'),
        ('SSHPU', 'Shop Units'),
        ('SCHL', 'School Building'),
        ('HSPTL', 'Hospital Building'),
        ('PTRLSTN', 'Petrol Station'),
        ('RSTRNT', 'Restaurant Building'),
        ]
    
    AVAILABLE = [
        ('Y', 'Yes'),
        ('N', 'No'),
        ]


    uploaded_by = GenericForeignKey('uploaded_by_content_type', 'uploaded_by_object_id')
    uploaded_by_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    uploaded_by_object_id = models.PositiveIntegerField()
    
    title = models.CharField(max_length=100)
    closest_landmark = models.CharField(max_length=50, blank=False, null=False, default=None)
    description = models.TextField(blank=False, null=False, default=None)

    property_id = models.CharField(max_length=50, unique=True, default=None)

    owned_by = models.CharField(max_length=50, blank=False, null=False, default=None, choices=OWNED_BY_STATUS)

    rent_price = models.DecimalField(max_digits=10, decimal_places=2)
    property_status = models.CharField(max_length=50, choices=PROPERTY_STATUS)
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPES)
    sub_commercial_property_type = models.CharField(max_length=50, blank=False, null=False, default=None, choices=SUB_COMMERCIAL_PROPERTY_TYPES)
    
    bathroom_is_available = models.CharField(max_length=50, blank=False, null=False, default=None, choices=AVAILABLE)
    toilet_is_available = models.CharField(max_length=50, blank=False, null=False, default=None, choices=AVAILABLE)
    water_is_available = models.CharField(max_length=50, blank=False, null=False, default=None, choices=AVAILABLE)
    good_power_supply = models.CharField(max_length=50, blank=False, null=False, default=None, choices=AVAILABLE)
    owner_lives_in_property = models.CharField(max_length=50, blank=False, null=False, default=None, choices=AVAILABLE)

    address = models.CharField(max_length=255, blank=False, null=False, default=None)
    city = models.CharField(max_length=100,blank=False, null=False, default=None)
    state = models.CharField(max_length=100, blank=False, null=False, default=None)
    zip_code = models.CharField(max_length=20)
    local_government = models.CharField(max_length=20, blank=False, null=False, default=None)
    
    date_time_of_upload = models.DateTimeField(auto_now_add=True)

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
