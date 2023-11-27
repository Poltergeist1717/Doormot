from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.views import View
from .forms import To_Let_Listed_Properties_Form, For_Sale_Listed_Properties_Form
from .models import To_Let_Listed_Properties, To_Let_Properties_Images, For_Sale_Listed_Properties, For_Sale_Properties_Images
from doormot_app.doormot_app_modules import return_user_object
from django.contrib.contenttypes.models import ContentType





def general_listing(request):
    user_type = request.session.get('user_type' )
    user_pk = request.session.get('user')
    user = return_user_object(user_pk, user_type)
    allowed_user_type = ['Individual_owner', 'Private_org_owner', 'Independent_agent', 'Official_agent']
    return render(request, 'doormot_property_listing/listing.html', {"title":"Listing", "user":user, 'user_type':user_type, 'allowed_user_type':allowed_user_type})




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

    def post(self, request):
        user_type = request.session.get('user_type', 'Individual_owner')
        user_pk = request.session.get('user')
        for_sale = request.session.get('for_sale')

        max_image_size = 1 * 1024 * 1024 

        allowed_user_type = ['Individual_owner', 'Private_org_owner', 'Independent_agent', 'Official_agent']
        if user_type not in allowed_user_type:
            print('You are not a recognized user!')
            return render(request, 'doormot_property_listing/listing.html', {"title": "Listing", "user": user, 'allowed_user_type': allowed_user_type})
        else:
            user = return_user_object(user_pk, user_type)

        # A form instance to avoid UnboundLocalError 
        # A name variable to avoid UnboundLocalError
        # UnboundLocalError (local variable referenced before assignment)
        form = To_Let_Listed_Properties_Form(request.POST, request.FILES) 
        name = "To Let Property" 
        

        if for_sale == "Yes":
            name = "For Sale Property"
            form = For_Sale_Listed_Properties_Form(request.POST, request.FILES)
        elif for_sale == "No":
            name = "To Let Property"
            form = To_Let_Listed_Properties_Form(request.POST, request.FILES)

        if request.method == 'POST':
            images = request.FILES.getlist('images')
            print(request.POST)

            if form.is_valid():
                try:
                    # Extract form data coomon to both fomrms
                    title = form.cleaned_data.get('title')
                    closest_landmark = form.cleaned_data.get('closest_landmark')
                    description = form.cleaned_data.get('description')
                    
                    address = form.cleaned_data.get('address')
                    city = form.cleaned_data.get('city')
                    state = form.cleaned_data.get('state')
                    zip_code = form.cleaned_data.get('zip_code')
                    local_government = form.cleaned_data.get('local_government')

                    # Additional fields for "Yes"
                    if for_sale == "Yes":
                        asking_price = form.cleaned_data.get('asking_price')
                        property_status = form.cleaned_data.get('property_status')
                        property_type = form.cleaned_data.get('property_type')

                        no_of_livingrooms = form.cleaned_data.get('no_of_livingrooms')
                        no_of_bedrooms = form.cleaned_data.get('no_of_bedrooms')
                        no_of_bathrooms = form.cleaned_data.get('no_of_bathrooms')
                        no_of_kitchens = form.cleaned_data.get('no_of_kitchens')

                        size_of_property_by_square_footage = form.cleaned_data.get('size_of_property_by_square_footage')
                        size_of_property_by_plot = form.cleaned_data.get('size_of_property_by_plot')
                        year_developed = form.cleaned_data.get('year_developed')

                    # Additional fields for "No"
                    elif for_sale == "No":
                        rent_price = form.cleaned_data.get('rent_price')
                        property_status = form.cleaned_data.get('property_status')
                        property_type = form.cleaned_data.get('property_type')
                        is_available_for_lease = form.cleaned_data.get('is_available_for_lease')

                        bathroom_is_available = form.cleaned_data.get('bathroom_is_available')
                        toilet_is_available = form.cleaned_data.get('toilet_is_available')
                        water_is_available = form.cleaned_data.get('water_is_available')
                        good_power_supply = form.cleaned_data.get('good_power_supply')
                        owner_lives_in_property = form.cleaned_data.get('owner_lives_in_property')

                    # Create property instance
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

                    elif for_sale == "No":
                        to_let_property_instance = To_Let_Listed_Properties.objects.create(
                            uploaded_by_content_type=ContentType.objects.get_for_model(user),
                            uploaded_by_object_id=user_pk,

                            title=title,
                            closest_landmark=closest_landmark,
                            description=description,

                            rent_price=rent_price,
                            property_status=property_status,
                            property_type=property_type,
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
                    
                    # Image handling
                    for image in images:
                        if not image.content_type.startswith('image'):
                            raise ValidationError("File is not an image. Please upload images only")

                        if image.size > max_image_size:
                            raise ValidationError("You cannot upload an image over 1MB in size!")

                        # Create image instance
                        if for_sale == "Yes":
                            property_image_instance = For_Sale_Properties_Images.objects.create(
                                connected_property=for_sale_property_instance,
                                images=image
                            )
                        elif for_sale == "No":
                            property_image_instance = To_Let_Properties_Images.objects.create(
                                connected_property=to_let_property_instance,
                                images=image
                            )

                except ValidationError as e:
                    # handle validation error
                    message = f"There was an error: {e}. Please try again."
                    return render(request, 'doormot_property_listing/upload_property.html',
                                  {'user': user, 'user_type': user_type, 'allowed_user_type': allowed_user_type,
                                   'form': form, 'name': name, 'message': message})
                except Exception as e:
                    message = f"There was an error: {e}. Please start over again!"
                    return render(request, 'doormot_property_listing/upload_property.html',
                                  {'user': user, 'user_type': user_type, 'allowed_user_type': allowed_user_type,
                                   'form': form, 'name': name, 'message': message})

                success_message = "Congratulations, you have uploaded a property successfully! " \
                                  "\nTo upload another property please answer if the property is for sale."
                return render(request, 'doormot_property_listing/upload_property.html',
                              {'user': user, 'user_type': user_type, 'allowed_user_type': allowed_user_type,
                               'form': form, 'name': name, 'success_message': success_message})

            else:
                form_error = form.errors
                message = f"Form validation Error: {form_error}! \nStart over \nPlease choose if the property is for sale."
                return render(request, 'doormot_property_listing/upload_property.html',
                              {'user': user, 'user_type': user_type, 'allowed_user_type': allowed_user_type,
                               'form': form,'name': name, 'message': message})
