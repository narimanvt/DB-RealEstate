from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=False)
    contact_person = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=64, null=False)
    client_details = models.TextField(null=False)

    def __str__(self):
        return f"Client with id {self.id}"


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    national_code = models.IntegerField(null=False)
    phone = models.IntegerField(null=False)

    def __str__(self):
        return f"Employee with id {self.id}"
    

class Contact(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False)
    estate = models.ForeignKey('Estates_and_Locations.Estate', on_delete=models.CASCADE, null=False)
    date = models.TimeField(null=True)
    detail = models.TextField(null=True)

    def __str__(self):
        return f"contact id {self.id}"