from django.shortcuts import render
from .doormot_app_modules import return_user_object
from doormot_property_listing.models import To_Let_Listed_Properties, For_Sale_Listed_Properties
from doormot_property_listing.modules import load_property_objects


def home(request):

    user = None
    user_type = request.session.get('user_type')
    user_pk = request.session.get('user')

    # place holder start
    for_sale = 'No'

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

    advertisied_property_models_filter_conditions = {}
    desired_max_price = 1000000.00 # placeholder
    advertisied_property_models_filter_conditions['rent_price__lte'] = desired_max_price

    advertisied_filtered_property_models = load_property_objects.get_filtered_queryset(model=model, filter_conditions=advertisied_property_models_filter_conditions)
    # placeholder ends
    
    user = return_user_object(user_pk, user_type)

    context =  {
        "title":"Home", 
        "user":user,
        'price_tag':price_tag,
        'for_sale':for_sale, 
        'advertisied_filtered_property_models':advertisied_filtered_property_models,
    }

    return render(request, 'doormot_app/home.html', context)


def about(request):

    user = None
    user_type = request.session.get('user_type')
    user_pk = request.session.get('user')

    user = return_user_object(user_pk, user_type)

    return render(request,'doormot_app/about.html', {"title":"About Us", 'user':user})


def team(request):
    user = None
    user_type = request.session.get('user_type')
    user_pk = request.session.get('user')

    user = return_user_object(user_pk, user_type)

    return render(request,'doormot_app/team.html', {"title":"Team", "user":user})

def contact(request):

    user = None
    user_type = request.session.get('user_type')
    user_pk = request.session.get('user')

    user = return_user_object(user_pk, user_type)

    return render(request,'doormot_app/contact.html', {"title":"Contact Us", "user":user})
