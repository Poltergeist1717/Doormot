from django.contrib import admin
from .models import Doormot_User_Individual_Owner, Doormot_User_Individual_Tenant, Doormot_User_Official_Agent, Doormot_User_Independent_Agent

class CustomUserAdmin(admin.ModelAdmin):
    list_diplay = ('username', 'email', 'phone_number', 'is_active', 'is_staff')

admin.site.register(Doormot_User_Individual_Tenant, CustomUserAdmin)
admin.site.register(Doormot_User_Official_Agent, CustomUserAdmin)
admin.site.register(Doormot_User_Independent_Agent, CustomUserAdmin)
admin.site.register(Doormot_User_Individual_Owner, CustomUserAdmin)