from django.contrib import admin
from .models import Client, Employee, Contact

admin.site.register(Employee)
admin.site.register(Client)
admin.site.register(Contact)