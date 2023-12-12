from django.shortcuts import render
from django.db import transaction
from django.core.exceptions import ValidationError
from django.views import View
from django.views.generic import ListView
from .forms import To_Let_Listed_Properties_Form, For_Sale_Listed_Properties_Form
from .models import To_Let_Listed_Properties, To_Let_Properties_Images, For_Sale_Listed_Properties, For_Sale_Properties_Images
from doormot_app.doormot_app_modules import return_user_object
from .modules import load_property_objects
from django.contrib.contenttypes.models import ContentType
from django.core.files.uploadedfile import SimpleUploadedFile
import imghdr
import logging

logger = logging.getLogger(__name__)





def general_listing(request):
    model = To_Let_Listed_Properties
    product_image_model = To_Let_Properties_Images

    for_sale = request.GET.get('for_sale') 
    desired_no_of_proprties_to_load = request.GET.get('desired_no_of_proprties_to_load')

    if for_sale == None:
        for_sale = 'No'

    if for_sale == 'No':
        model = To_Let_Listed_Properties
    if for_sale == 'Yes':
        model = For_Sale_Listed_Properties

    price_tag = "Rent"
    if for_sale == 'No':
        price_tag = "Rent"
    if for_sale == 'Yes':
        price_tag = "Asking"

    if for_sale == None:
        price_tag = "Rent"


    user_type = request.session.get('user_type' )
    user_pk = request.session.get('user')
    user = return_user_object(user_pk, user_type)
    allowed_user_type = ['Individual_owner', 'Private_org_owner', 'Independent_agent', 'Official_agent']
    
    properties = load_property_objects(model=model)
    batch_properties = properties.load_property_models_in_batches(desired_no_of_proprties_to_load=desired_no_of_proprties_to_load)
    def return_property_model(batch_properties):
        for property_models in batch_properties:
           return property_models

    property_models = return_property_model(batch_properties)
    return render(request, 'doormot_property_listing/listing.html', {"title":"Listing", "user":user, 'user_type':user_type, 'allowed_user_type':allowed_user_type, 'property_models':property_models, "price_tag":price_tag, 'for_sale':for_sale})




# Type: Class
# Name: Post Property View
# Methods: get, post, validate_images, create_property_instance, handle_image_creation
# Tasks: Handles uploading property
#        Handles upload logic for property types
#        Prevents users not allowed to upload property
#        Reverse changes made to database if any of the transactions fails (@transaction.atomic) 
#        Handles creating property instnance for both types - For Sale and To Let
#        Handles creating property image instance for both types - For Sale and To Let
#        Resets False log count field to default

class post_property(View):
    def get(self, request):
        for_sale = request.GET.get('for_sale')
        request.session['for_sale'] = for_sale
        allowed_user_type = ['Individual_owner', 'Private_org_owner', 'Independent_agent', 'Official_agent']

        user_type = request.session.get('user_type')
        user_pk = request.session.get('user')
        user = return_user_object(user_pk, user_type)

        form = None # Create a None form variable to avoid UnboundLocalError 
        name = None # Create a None name variable to avoid UnboundLocalError
        # UnboundLocalError (local variable referenced before assignment)

        if for_sale == "Yes":
            name = "For Sale Property"
            form = For_Sale_Listed_Properties_Form(request.POST, request.FILES)
        elif for_sale == "No":
            name = "To Let Property"
            form = To_Let_Listed_Properties_Form(request.POST, request.FILES)
        else:
            name = "None"
            form = None
        return render(request, 'doormot_property_listing/upload_property.html', {'user': user, 'user_type': user_type, 'allowed_user_type': allowed_user_type, 'form': form, 'name': name, 'for_sale':for_sale})

    @transaction.atomic
    def post(self, request):
        user_type = request.session.get('user_type', 'Individual_owner')
        user_pk = request.session.get('user')
        for_sale = request.session.get('for_sale')

        allowed_user_type = ['Individual_owner', 'Private_org_owner', 'Independent_agent', 'Official_agent']

        if user_type not in allowed_user_type:
            return render(request, 'doormot_property_listing/listing.html', {"title": "Listing", "user": user, 'allowed_user_type': allowed_user_type})
        else:
            user = return_user_object(user_pk, user_type)

        form = To_Let_Listed_Properties_Form(request.POST, request.FILES)
        name = "To Let Property"

        if for_sale == "Yes":
            name = "For Sale Property"
            form = For_Sale_Listed_Properties_Form(request.POST, request.FILES)

        if request.method == 'POST':
            images = request.FILES.getlist('images')

            if form.is_valid():
                try:
                    validate_images = self.validate_images(images=images)
                    print(validate_images) 
                    returned_property_instance = self.create_property_instance(for_sale=for_sale, user=user, user_pk=user_pk, form=form)
                    for image_data in validate_images:
                        print(image_data)
                        self.handle_image_creation(for_sale=for_sale, images=image_data, property_instance=returned_property_instance)                   
                except ValidationError as e:
                    message = f"There was Validation error(s): {e}. Please try again."
                    return render(request, 'doormot_property_listing/upload_property.html', {'user': user, 'user_type': user_type, 'allowed_user_type': allowed_user_type, 'form': form, 'name': name, 'message': message})
                except Exception as e:
                    message = f"There was Exception error(): {e}. Please start over again!"
                    return render(request, 'doormot_property_listing/upload_property.html', {'user': user, 'user_type': user_type, 'allowed_user_type': allowed_user_type, 'form': form, 'name': name, 'message': message})

                success_message = "Congratulations, you have uploaded a property successfully!"
                return render(request, 'doormot_property_listing/upload_property.html', {'user': user, 'user_type': user_type, 'allowed_user_type': allowed_user_type, 'form': form, 'name': name, 'success_message': success_message})

            else:
                form_error = form.errors
                values = form_error.values()
                message = f"Form validation Error(s):"
                return render(request, 'doormot_property_listing/upload_property.html', {'user': user, 'user_type': user_type, 'allowed_user_type': allowed_user_type, 'form': form, 'name': name, 'message': message, 'values': values})

    def validate_images(self, images):
        max_image_size = 1 * 1024 * 1024
        max_image_count = 12
        image_list = []

        if len(images) > max_image_count:
            raise ValidationError("You can only upload 12 images per property!")

        for image in images:
            if not image.content_type.startswith('image'):
                raise ValidationError(f"Invalid file type. Please upload images only!. {image} is not a valid file type!")

            if image.size > max_image_size:
                raise ValidationError(f"Image size cannot exceed 1MB. {image} is too large!")
                        
            image_list.append(image)

        return image_list          


    def create_property_instance(self, for_sale, user, user_pk, form):
        try:
            # Extract form data coomon to both fomrms
            title = form.cleaned_data.get('title')
            closest_landmark = form.cleaned_data.get('closest_landmark')
            description = form.cleaned_data.get('description')
            owned_by = form.cleaned_data.get('owned_by')
                    
            address = form.cleaned_data.get('address')
            city = form.cleaned_data.get('city')
            state = form.cleaned_data.get('state')
            zip_code = form.cleaned_data.get('zip_code')
            local_government = form.cleaned_data.get('local_government')
            property_type = form.cleaned_data.get('property_type')
            sub_commercial_property_type = form.cleaned_data.get('sub_commercial_property_type')

            # Additional fields for "Yes"
            if for_sale == "Yes":
                asking_price = form.cleaned_data.get('asking_price')
                property_status = form.cleaned_data.get('property_status')
                

                no_of_livingrooms = form.cleaned_data.get('no_of_livingrooms')
                no_of_bedrooms = form.cleaned_data.get('no_of_bedrooms')
                no_of_bathrooms = form.cleaned_data.get('no_of_bathrooms')
                no_of_kitchens = form.cleaned_data.get('no_of_kitchens')

                size_of_property_by_square_footage = form.cleaned_data.get('size_of_property_by_square_footage')
                size_of_property_by_plot = form.cleaned_data.get('size_of_property_by_plot')
                year_developed = form.cleaned_data.get('year_developed')
                is_negotiable = form.cleaned_data.get('is_negotiable')

            # Additional fields for "No"
            elif for_sale == "No":
                rent_price = form.cleaned_data.get('rent_price')
                property_status = form.cleaned_data.get('property_status')
                is_available_for_lease = form.cleaned_data.get('is_available_for_lease')

                bathroom_is_available = form.cleaned_data.get('bathroom_is_available')
                toilet_is_available = form.cleaned_data.get('toilet_is_available')
                water_is_available = form.cleaned_data.get('water_is_available')
                good_power_supply = form.cleaned_data.get('good_power_supply')
                owner_lives_in_property = form.cleaned_data.get('owner_lives_in_property')
                
            
            if for_sale == "Yes":
                for_sale_property_instance = For_Sale_Listed_Properties.objects.create(
                    uploaded_by_content_type=ContentType.objects.get_for_model(user),
                    uploaded_by_object_id=user_pk,

                    title=title,
                    closest_landmark=closest_landmark,
                    description=description,

                    asking_price=asking_price,
                    property_status=property_status,
                    property_type=property_type,
                    sub_commercial_property_type=sub_commercial_property_type,
                    owned_by = owned_by,

                    no_of_livingrooms=no_of_livingrooms,
                    no_of_bedrooms=no_of_bedrooms,
                    no_of_bathrooms=no_of_bathrooms,
                    no_of_kitchens=no_of_kitchens,

                    size_of_property_by_square_footage=size_of_property_by_square_footage,
                    size_of_property_by_plot=size_of_property_by_plot,
                    year_developed = year_developed,

                    address=address,
                    city=city,
                    state=state,
                    zip_code=zip_code,
                    local_government=local_government,
                    )
                # Save property instance - For Sale
                for_sale_property_instance.save()
                return for_sale_property_instance
                        
            elif for_sale == "No":
                to_let_property_instance = To_Let_Listed_Properties.objects.create(
                    uploaded_by_content_type=ContentType.objects.get_for_model(user),
                    uploaded_by_object_id=user_pk,

                    title=title,
                    closest_landmark=closest_landmark,
                    description=description,
                    owned_by = owned_by,

                    rent_price=rent_price,
                    property_status=property_status,
                    property_type=property_type,
                    sub_commercial_property_type=sub_commercial_property_type,
                    is_available_for_lease=is_available_for_lease,

                    bathroom_is_available=bathroom_is_available,
                    toilet_is_available=toilet_is_available,
                    water_is_available=water_is_available,
                    good_power_supply=good_power_supply,
                    owner_lives_in_property=owner_lives_in_property,

                    address=address,
                    city=city,
                    state=state,
                    zip_code=zip_code,
                    local_government=local_government,
                    )
                # Save property instance - To Let
                to_let_property_instance.save()
                return to_let_property_instance
        except Exception as e:
            message = f"There was Exception error(s) during creating property instance: {e}. Please start over again!"
            logger.exception(message)

    def handle_image_creation(self, for_sale, images, property_instance):
        self.for_sale = for_sale
        self.property_instance = property_instance
        self.images = images
        try:        
            if self.for_sale == "Yes":
                property_image_instance = For_Sale_Properties_Images.objects.create(
                    connected_property = self.property_instance,
                    images = self.images
                    )
                print(f"For sale property image instance: {property_image_instance}")
            elif self.for_sale == "No":
                property_image_instance = To_Let_Properties_Images.objects.create(
                    connected_property = self.property_instance,
                    images = self.images
                    )
                print(f"To let property image instance: {property_image_instance}")
        except Exception as e:
            message = f"There was Exception error(s) during creating property image instance: {e}. Please start over again!"
            logger.exception(message)









# Type: Class
# Name: Filter Property View
# Methods: get_queryset, get_context_data
# Tasks: Handles filtering property queryset
#        Handles upload logic for property types
#        Prevents users not allowed to upload property
#        Reverse changes made to database if any of the transactions fails (@transaction.atomic) 
#        Handles creating property instnance for both types - For Sale and To Let
#        Handles creating property image instance for both types - For Sale and To Let
#        Resets False log count field to default


class filtered_property_view(ListView):   
    template_name = 'doormot_property_listing/filtered_properties.html'
    context_object_name = 'filtered_property_models'

    def get_context_data(self, **kwargs):
        user_type = self.request.session.get('user_type' )
        user_pk = self.request.session.get('user')        
        user = return_user_object(user_pk, user_type)
        for_sale = self.request.session.get('for_sale')
        filter_conditions = self.request.session.get('filter_conditions')

        allowed_user_type = ['Individual_owner', 'Private_org_owner', 'Independent_agent', 'Official_agent']
                
        context = super().get_context_data(**kwargs)

        price_tag = "Rent"
        if for_sale == 'No':
            price_tag = "Rent"
            filter_property_tag = "To Let"
        if for_sale == 'Yes':
            price_tag = "Asking"
            filter_property_tag = "For Sale"

        context['title'] = 'Filtered Properties'
        context['user'] = user
        context['allowed_user_type'] = allowed_user_type
        context['user_type'] = user_type
        context['for_sale'] = for_sale
        context['price_tag'] = price_tag
        context['filter_conditions'] = filter_conditions
        context['filter_property_tag'] = filter_property_tag
        return context
    

    def get_queryset(self):

        for_sale = self.request.GET.get('for_sale')
        self.request.session['for_sale'] = for_sale

        print(f"for_sale inside get queryset: {for_sale}")

        
        if for_sale == 'No':
            model = To_Let_Listed_Properties
        elif for_sale == 'Yes':
            model = For_Sale_Listed_Properties
        else:
            model = To_Let_Listed_Properties
        
        filter_conditions = {}   

        desired_town_city = self.request.GET.get('city')
        desired_state = self.request.GET.get('state')
        desired_local_governmet = self.request.GET.get('local_government')
        owned_by = self.request.GET.get('owned_by')
        property_type = self.request.GET.get('property_type')
        property_ID = self.request.GET.get('property_id')
        zip_code = self.request.GET.get('zip_code')
        property_status = self.request.GET.get('property_status')
        desired_min_price = float(self.request.GET.get('min_price', 0))
        desired_max_price = float(self.request.GET.get('max_price', float('inf')))
            
        print(property_ID)
        
        sub_commercial_property_type = ''

        if property_type == "Commercial Building":
            sub_commercial_property_type = self.request.GET.get('sub_commercial_property_type')

        if for_sale == "Yes":
            is_negotiable = self.request.GET.get('is_negotiable')
                        
            # Asking price
            if desired_min_price:
                filter_conditions['asking_price__gte'] = desired_min_price

            if desired_max_price:
                filter_conditions['asking_price__lte'] = desired_max_price

            if is_negotiable is not None:
                filter_conditions['is_negotiable'] = is_negotiable

            if property_ID:
                filter_conditions['property_id'] = property_ID




        if for_sale == "No":
            owner_lives_in_property = self.request.GET.get('owner_lives_in_property')
            good_power_supply = self.request.GET.get('good_power_supply')
            toilet_is_available = self.request.GET.get('toilet_is_available')
            is_available_for_lease = self.request.GET.get('available_for_lease')
            
            # Rent price
            if desired_min_price:
                filter_conditions['rent_price__gte'] = desired_min_price

            if desired_max_price:
                filter_conditions['rent_price__lte'] = desired_max_price

           
            if owner_lives_in_property is not None:
                filter_conditions['owner_lives_in_property'] = owner_lives_in_property

            if good_power_supply is not None:
                filter_conditions['good_power_supply'] = good_power_supply

            if toilet_is_available is not None:
                filter_conditions['toilet_is_available'] = toilet_is_available


            if is_available_for_lease is not None:
                filter_conditions['is_available_for_lease'] = is_available_for_lease

            if property_ID:
                filter_conditions['property_id'] = property_ID

       
        
        if desired_town_city != '':
            filter_conditions['city'] = desired_town_city

        if desired_state != '':
            filter_conditions['state'] = desired_state
        
        if desired_local_governmet != '':
            filter_conditions['local_government'] = desired_local_governmet

        if owned_by != '':
            filter_conditions['owned_by'] = owned_by

        if property_type != '':
            filter_conditions['property_type'] = property_type

        if sub_commercial_property_type != '':
            filter_conditions['sub_commercial_property_type'] = sub_commercial_property_type

        if property_status != '':
            filter_conditions['property_status'] = property_status

        if zip_code != '':
            filter_conditions['zip_code'] = zip_code

        
        print (filter_conditions)
        self.request.session['filter_conditions'] = filter_conditions 

        return load_property_objects.get_filtered_queryset(model=model, filter_conditions=filter_conditions)


def property_more_details(request):
    
    for_sale = request.GET.get('for_sale')
    print(for_sale)
        
    if for_sale == 'No':
        model = To_Let_Listed_Properties
        price_tag = "Rent"
        filter_property_tag = "To Let"
    elif for_sale == 'Yes':
        model = For_Sale_Listed_Properties
        price_tag = "Asking"
        filter_property_tag = "For Sale"
    else:
        model = To_Let_Listed_Properties
        price_tag = "Rent"
        filter_property_tag = "To Let"

    filter_conditions = {}
    properprty_id = request.GET.get("property_model_id")

    if properprty_id:
        filter_conditions["id"] = properprty_id

    property_model = load_property_objects.get_filtered_queryset(model=model, filter_conditions=filter_conditions)
    print(property_model)
    for properties in property_model:
        print(properties.address)
    
    return render(request, 'doormot_property_listing/property_more_details.html', {'title':'Property Details', 'property_model':property_model, 'price_tag':price_tag})