from django.shortcuts import render


def home(request):
    return render(request, 'doormot_app/home.html', {"title":"Home"} )

def about(request):
    return render(request,'doormot_app/about.html', {"title":"About Us"})

def listing(request):
    return render(request,'doormot_app/listing.html', {"title":"Property Listing"})

def team(request):
    return render(request,'doormot_app/team.html', {"title":"Team"})

def contact(request):
    return render(request,'doormot_app/contact.html', {"title":"Contact Us"})
