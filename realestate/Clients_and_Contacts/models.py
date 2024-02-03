from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    national_code = models.IntegerField(null=False, unique=True, primary_key =True)
    address = models.CharField(max_length=255, null=False)
    contact_person = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=64, null=False)
    email = models.EmailField(null=True)
    client_details = models.TextField(null=True)
    username = models.CharField(max_length=64, null=False)
    password = models.CharField(max_length =64, null=False)

    def __str__(self):
        return f"Client with id {self.id}"

class Employee(models.Model):
    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=True)
    national_code = models.IntegerField(null=False, unique=True)
    phone_number = models.IntegerField(null=False, unique=True)

    def __str__(self):
        return f"Employee with id {self.id}"
    
class Contact(models.Model):
    client_id =  models.ForeignKey(Client, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False)
    estate = models.ForeignKey('Estates_and_Locations.Estate', on_delete=models.CASCADE, null=False)
    contact_time = models.TimeField(null=True)
    detail = models.TextField(null=True)

    def __str__(self):
        return f"contact id {self.id}"