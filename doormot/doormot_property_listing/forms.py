from django import forms
from django.core.exceptions import ValidationError
from PIL import Image
from .models import To_Let_Listed_Properties, For_Sale_Listed_Properties


class To_Let_Listed_Properties_Form(forms.ModelForm):

    class Meta:
     
        model = To_Let_Listed_Properties
        fields = [
            "title",
            "description",
            "rent_price",
            "owned_by",
            "address",            
            "zip_code",
        ]




class For_Sale_Listed_Properties_Form(forms.ModelForm):

    class Meta:
        model = For_Sale_Listed_Properties
        fields = [
            "title",
            "description",
            "asking_price",            
            "owned_by",
            "address",
            "zip_code",
        ]

