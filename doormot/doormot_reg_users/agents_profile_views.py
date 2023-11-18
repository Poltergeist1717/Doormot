from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from .forms import Individual_owner_registeration_form, Individual_Tenant_Registration_Form, Private_Organization_Tenant_Registration_Form, Official_Agent_Registration_Form, Official_Agent_Next_Of_Kin_Registration_Form, Official_Agent_Guarantor_Registration_Form, Doormot_User_Independent_Agent_Form 




def official_agent(request):
    form = Official_Agent_Registration_Form()
    next_of_kin_form = Official_Agent_Next_Of_Kin_Registration_Form()
    guarantor_form = Official_Agent_Guarantor_Registration_Form()

    if request.method == 'POST':
        form = Official_Agent_Registration_Form(request.POST)
        next_of_kin_form = Official_Agent_Next_Of_Kin_Registration_Form(request.POST)
        guarantor_form = Official_Agent_Guarantor_Registration_Form(request.POST)

        if form.is_valid():
            profile = form.save()
            profile = next_of_kin_form()
            profile = guarantor_form.save()
            return redirect('doormot-login')
        else:
            form = Official_Agent_Registration_Form()
            next_of_kin_form = Official_Agent_Next_Of_Kin_Registration_Form()
            guarantor_form = Official_Agent_Guarantor_Registration_Form()
        
            
    return render(request, 'doormot_reg_users/official_agent.html', {'title':'Official-Agent-registration', 'form':form, 'next_of_kin_form':next_of_kin_form, 'guarantor_form':guarantor_form})
