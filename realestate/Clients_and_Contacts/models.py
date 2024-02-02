from django.db import models
from django.contrib.auth.models import User


class PhoneNumber(models.Model):
    PHONE_TYPES = (
        ("Mobile", "Mobile"),
        ("Work", "Work"),
        ("Home", "Home")
    )
    phone_number = models.CharField(max_length=20)
    phone_type = models.CharField(max_length=6, choices=PHONE_TYPES, default="Mobile")


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    national_code = models.IntegerField(null=False, unique=True)
    address = models.CharField(max_length=255, null=False)
    contact_person = models.CharField(max_length=255, null=False)
    phone_number = models.ForeignKey(PhoneNumber, on_delete=models.CASCADE, blank=True, null=True, choices=PhoneNumber.PHONE_TYPES)

    def get_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        return f"Client with id {self.id}"


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    national_code = models.IntegerField(null=False, unique=True)
    phone_number = models.ForeignKey(PhoneNumber, on_delete=models.CASCADE, blank=True, null=True, choices=PhoneNumber.PHONE_TYPES)

    def get_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        return f"Employee with id {self.id}"
    

class Contact(models.Model):
    client_offered = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='offered_contact', null=False)
    client_requested = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='requested_contact', null=False) 
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False)
    estate = models.ForeignKey('Estates_and_Locations.Estate', on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(null=True)
    detail = models.TextField(null=True)

    def __str__(self):
        return f"contact id {self.id}"