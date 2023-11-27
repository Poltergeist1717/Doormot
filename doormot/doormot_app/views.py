from django.shortcuts import render
from .doormot_app_modules import return_user_object


def home(request):

    user = None
    user_type = request.session.get('user_type')
    user_pk = request.session.get('user')
    
    user = return_user_object(user_pk, user_type)

    return render(request, 'doormot_app/home.html', {"title":"Home", "user":user})


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
