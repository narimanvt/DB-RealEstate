from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth import get_user_model
#User=get_user_model()

class PhoneNumber(models.Model):
    PHONE_TYPES = (
        ("Mobile", "Mobile"),
        ("Work", "Work"),
        ("Home", "Home")
    )
    phone_number = models.CharField(max_length=20)
    phone_type = models.CharField(max_length=6, choices=PHONE_TYPES, default="Mobile")


class Client(models.Model):
    #first_name = models.ForeignKey(User, 'User.first_name', on_delete=models.CASCADE)
    #last_name = models.ForeignKey(User, 'User.last_name', on_delete=models.CASCADE)
    #email = models.ForeignKey(User, 'User.email', on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    national_code = models.IntegerField(null=False, unique=True)
    address = models.CharField(max_length=255, null=False)
    contact_person = models.CharField(max_length=255, null=False)
    phone = models.ManyToManyField(PhoneNumber, blank=True, choices=PhoneNumber.PHONE_TYPES)
    client_details = models.TextField(null=False)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"Client with id {self.id}"


class Employee(models.Model):
    #first_name = models.ForeignKey(User, 'User.first_name', on_delete=models.CASCADE)
    #last_name = models.ForeignKey(User, 'User.last_name', on_delete=models.CASCADE)
    #email = models.ForeignKey(User, 'User.email', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    national_code = models.IntegerField(null=False, unique=True)
    phone = models.ManyToManyField(PhoneNumber, blank=True, choices=PhoneNumber.PHONE_TYPES)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

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