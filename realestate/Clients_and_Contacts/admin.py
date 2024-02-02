from django.contrib import admin
from .models import PhoneNumber, Client, Employee, Contact

# Register models with the custom admin classes

@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'phone_type')
    search_fields = ['phone_number']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'phone_number')
    search_fields = ['user__first_name', 'user__last_name', 'phone']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'phone_number', 'address')
    search_fields = ['user__first_name', 'user__last_name', 'phone']
    

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('client_offered', 'client_requested', 'employee', 'estate', 'date')
    list_filter = ('client_offered', 'client_requested', 'employee', 'estate', 'date')
    search_fields = ['client_offered', 'client_requested', 'employee', 'estate', 'date']