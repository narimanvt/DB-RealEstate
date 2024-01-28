from django.contrib import admin
from .models import Address, Estate, In_charge

# Register your models with the custom admin classes

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('state', 'city', 'street')
    list_filter = ('state', 'city', 'street')
    search_fields = ['state', 'city', 'street']

@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
    list_display = ('estate_type', 'estate_status', 'year_of_construction')
    list_filter = ('estate_type', 'estate_status', 'year_of_construction')
    search_fields = ['estate_type', 'estate_status', 'year_of_construction']

@admin.register(In_charge)
class InChargeAdmin(admin.ModelAdmin):
    list_display = ('estate', 'employee')
    list_filter = ('estate', 'employee')