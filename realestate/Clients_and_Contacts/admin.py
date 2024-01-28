from django.contrib import admin
from .models import Client, Employee, Contact

# Register models with the custom admin classes

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'national_code', 'phone')
    list_filter = ('first_name', 'last_name')
    search_fields = ['first_name', 'last_name', 'phone']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'address')
    list_filter = ('first_name', 'last_name')
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('client', 'employee', 'estate', 'date')
    list_filter = ('client', 'employee', 'estate', 'date')
    search_fields = ['client', 'employee', 'estate', 'date']