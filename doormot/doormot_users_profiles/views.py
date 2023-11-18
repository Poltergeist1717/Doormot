from django.shortcuts import render

def individual_owner_profile_view(request):
    return render(request, 'doormot_users_profiles/individual_owner_profile.html', {"title":"Individual-Owner-Profile"})