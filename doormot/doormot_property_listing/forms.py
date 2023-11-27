from django import forms
from django_countries.fields import CountryField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, HTML, Submit
from django.core.exceptions import ValidationError
from PIL import Image
from .models import To_Let_Listed_Properties, For_Sale_Listed_Properties


class To_Let_Listed_Properties_Form(forms.ModelForm):

    class Meta:
        title = forms.CharField(
            label = "Title:",
            widget = forms.TextInput(),
        )

        closest_landmark = forms.CharField(
            label = "Closest Landmark:",
            widget = forms.TextInput(),
        )

       

        model = To_Let_Listed_Properties
        fields = [
            "title",
            "closest_landmark",
            "description",

            "rent_price",
            "property_status",
            "property_type",
            "is_available_for_lease",

            "bathroom_is_available",
            "toilet_is_available",
            "water_is_available",
            "good_power_supply",
            "owner_lives_in_property",

            "address",
            "city",
            "state",
            "zip_code",
            "local_government",
        ]




class For_Sale_Listed_Properties_Form(forms.ModelForm):

    year_developed = forms.DateField(
            label = "Year Property was Developed:",
            widget = forms.DateInput(attrs={'type':'date'}),
        )

    class Meta:
        model = For_Sale_Listed_Properties
        fields = [
            "title",
            "closest_landmark",
            "description",

            "asking_price",
            "property_status",
            "property_type",

           "no_of_livingrooms",
            "no_of_bedrooms",
            "no_of_bathrooms",
            "no_of_kitchens",

            "size_of_property_by_square_footage",
            "size_of_property_by_plot",
            "year_developed",

            "address",
            "city",
            "state",
            "zip_code",
            "local_government",
        ]

