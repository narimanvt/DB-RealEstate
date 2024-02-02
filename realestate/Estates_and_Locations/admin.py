from django.contrib import admin
from .models import (
    Estate_type,
    Estate_status,
    Country,
    City,
    Address,
    Estate,
    In_charge,
)

@admin.register(Estate_type)
class EstateTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name', )
    search_fields = ['type_name']

@admin.register(Estate_status)
class EstateStatusAdmin(admin.ModelAdmin):
    list_display = ('estate_status_name', )
    search_fields = ['estate_status_name']

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_name', )
    list_filter = ('country_name', )
    search_fields = ['country_name']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city_name', )
    list_filter = ('city_name', )
    search_fields = ['city_name']

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('state', 'city', 'street')
    list_filter = ('state', 'city', 'street')
    search_fields = ['state', 'city', 'street']

@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
    list_display = ('estate_type_id', 'estate_status_id', 'year_of_construction')
    list_filter = ('estate_type_id', 'estate_status_id', 'year_of_construction')
    search_fields = ['estate_type_id', 'estate_status_id', 'year_of_construction']

@admin.register(In_charge)
class InChargeAdmin(admin.ModelAdmin):
    list_display = ('estate', 'employee')
    list_filter = ('estate', 'employee')