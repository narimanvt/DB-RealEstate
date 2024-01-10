from django.contrib import admin
from .models import Estate, City, Country, Estate_type, Estate_status, In_charge

admin.site.register(Estate)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Estate_status)
admin.site.register(Estate_type)
admin.site.register(In_charge)