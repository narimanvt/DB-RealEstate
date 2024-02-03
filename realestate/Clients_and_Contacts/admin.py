from django.contrib import admin
from .models import  Client, Employee, Contact

# Register models with the custom admin classes


admin.site.register(Employee)
admin.site.register(Client)
admin.site.register(Contact)
