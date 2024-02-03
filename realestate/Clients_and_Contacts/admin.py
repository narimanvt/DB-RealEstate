from django.contrib import admin
from .models import (
    Client,
    Employee,
    Contact
)

# Register models with the custom admin classes
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'national_code', 'phone_number', 'email', 'username', 'password')
    list_filter = ('first_name', 'last_name', 'username')
    search_fields = ['first_name', 'last_name', 'national_code', 'phone_number', 'email', 'username', 'password']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'national_code', 'phone_number', 'email', 'username', 'password')
    list_filter = ('first_name', 'last_name', 'username')
    search_fields = ['first_name', 'last_name', 'national_code', 'phone_number', 'email', 'username', 'password']

# @admin.register(Contact)
# class ContactAdmin(admin.ModelAdmin):
#     list_display = ('client', 'employee', 'estate', 'date')
#     list_filter = ('client', 'employee', 'estate', 'date')
#     search_fields = ['client', 'employee', 'estate', 'date']

admin.site.register(Contact)