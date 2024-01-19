from django.contrib import admin
from .models import Address, Estate, In_charge

# Register your models with the custom admin classes

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('State', 'City', 'Street')
    list_filter = ('State', 'City', 'Street')
    search_fields = ['State', 'City', 'Street']

@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
    list_display = ('Estate Type', 'Estate Status', 'Year Of Construction')
    list_filter = ('Estate Type', 'Estate Status', 'Year Of Construction')
    search_fields = ['Estate Type', 'Estate Status', 'Year Of Construction']

@admin.register(In_charge)
class InChargeAdmin(admin.ModelAdmin):
    list_display = ('Estate', 'Employee')
    list_filter = ('Estate', 'Employee')