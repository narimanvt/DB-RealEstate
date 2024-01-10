from django.db import models

# Create your models here.

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=255, null=False)
    client_address = models.CharField(max_length=255, null=False)
    contact_person = models.CharField(max_length=255, null=False)
    phone= models.CharField(max_length=64, null=False)
    mobile = models.CharField(max_length=64, null=False)
    mail = models.EmailField(null=True)
    client_details = models.TextField(null=False)

    def __str__(self):
        return f"Client with id {self.id}"


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=False)
    national_code = models.IntegerField(null=False)
    
    def __str__(self):
        return f"Employee with id {self.id}"
    

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    client_id = models.IntegerField(null=False) 
    employee_id = models.IntegerField(null=False)
    estate_id = models.IntegerField(null=False)
    contact_time = models.TimeField(null=True)
    contact_detail = models.TextField(null=True)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, null=False)
    estate_id = models.ForeignKey(Estate, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"contact id {self.id}"