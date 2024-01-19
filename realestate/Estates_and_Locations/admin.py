from django.contrib import admin
from .models import Estate, City, Country, Estate_type, Estate_status, In_charge

# Register your models with the custom admin classes

@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'bedrooms', 'bathrooms', 'status', 'type', 'in_charge')
    search_fields = ['title', 'in_charge__name']  # Add fields you want to search

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ['name', 'country__name']  # Add fields you want to search

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Estate_status)
class EstateStatusAdmin(admin.ModelAdmin):
    list_display = ('status',)

@admin.register(Estate_type)
class EstateTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)

@admin.register(In_charge)
class InChargeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')




#admin.site.register(Estate)
#admin.site.register(City)
#admin.site.register(Country)
#admin.site.register(Estate_status)
#admin.site.register(Estate_type)
#admin.site.register(In_charge)