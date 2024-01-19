from django.contrib import admin
from .models import Client, Employee, Contact

# Register models with the custom admin classes

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('First Name', 'Last Name', 'National Code', 'Phone')
    list_filter = ('First Name', 'Last Name')
    search_fields = ['First Name', 'Last Name', 'Phone']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('First Name', 'Last Name', 'E-mail', 'Phone', 'Address')
    list_filter = ('First Name', 'Last Name')
    search_fields = ['First Name', 'Last Name', 'E-mail', 'Phone']
    

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('Client_id', 'Employee_id', 'Estate_id', 'Contact Time')
    list_filter = ('Client_id', 'Employee_id', 'Estate_id', 'Contact Time')
    search_fields = ['Client_id', 'Employee_id', 'Estate_id', 'Contact Time']