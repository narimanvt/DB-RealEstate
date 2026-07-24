from django.contrib import admin
from .models import (
    Client,
    Employee,
    Contact
)

# Register models with the custom admin classes.
# Note: `password` is intentionally excluded from list_display/search_fields -
# it is stored in plaintext (see README "Known Limitations"), so it should
# never be rendered or made searchable in the admin UI.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'national_code', 'phone_number', 'email', 'username')
    list_filter = ('first_name', 'last_name', 'username')
    search_fields = ['first_name', 'last_name', 'national_code', 'phone_number', 'email', 'username']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'national_code', 'phone_number', 'email', 'username')
    list_filter = ('first_name', 'last_name', 'username')
    search_fields = ['first_name', 'last_name', 'national_code', 'phone_number', 'email', 'username']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('Client', 'employee', 'estate', 'date')
    list_filter = ('date',)
    search_fields = ['Client__first_name', 'Client__last_name', 'employee__first_name', 'employee__last_name']