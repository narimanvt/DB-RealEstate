from django.db import models
from Clients_and_Contacts.models import Client, Employee

# Create your models here.
#class Transaction_type(models.Model):
#    id = models.AutoField(primary_key=True)
#    transaction_type_name = models.CharField(max_length=64, null=False)
#    def __str__(self):
#        return f"{self.transaction_type_name}"
    

#class Transaction(models.Model):
#    id = models.AutoField(primary_key=True)  
#    transaction_type = models.ForeignKey(Transaction_type, on_delete = models.CASCADE, null=False)
#    client_offered = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='offered_transactions', null=False)
#    client_requested = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='requested_transactions', null=False) 
#    transaction_date = models.DateField(null=False)
#    transaction_details = models.TextField(null=True)
    
#    def __str__(self):
#        return f"Transaction with id {self.id}"

class Transaction(models.Model):

    TRANSACTION_TYPES = (
        ("Buy", "Buy"),
        ("Rent", "Rent"),
        ("Barter", "Barter"),
        ("Mortgage", "Mortgage"),
        ("Pre-Sale", "Pre-Sale")
        ("Lease And Rent", "Lease And Rent"),
    )

    id = models.AutoField(primary_key=True)  
    Transaction_type = models.CharField(max_length=128, null=False, choices=TRANSACTION_TYPES.choices)
    client_offered = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='offered_transactions', null=False)
    client_requested = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='requested_transactions', null=False) 
    transaction_date = models.DateField(null=False)
    transaction_details = models.TextField(null=True)
                  

    def __str__(self):
        return f"Transaction with id {self.id}"



#class Payment_frequency(models.Model):
#    id = models.AutoField(primary_key=True)
#    payment_frequency_name = models.CharField(max_length=64, null=False)

#    def __str__(self):
#        return f"{self.payment_frequency_name}"
    

class Contract_type(models.Model):
    id = models.AutoField(primary_key=True)
    contract_type_name = models.CharField(max_length=64, null=False)
    fee_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=False)

    def __str__(self):
        return f"{self.contract_type_name}"


class Contract(models.Model):
    id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, null=False)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False)
    contract_type = models.ForeignKey(Contract_type, on_delete=models.CASCADE, null=False)
    contract_details = models.TextField(null=True)
#############3
    estate_id = models.IntegerField(null=False)
##########################
    payment_frequency_name = models.CharField(max_length=64, null=False)
    ###################################
#    payment_frequency = models.ForeignKey(Payment_frequency, on_delete=models.CASCADE, null=False)
    number_of_invoices = models.IntegerField(null=False)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    fee_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    fee_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    date_signed = models.DateField(null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    transaction_id = models.ForeignKey(Transaction, on_delete=models.CASCADE, null=False)

    def __str__(self) :
        return f"Contract with id {self.id}"


class Contract_invoice(models.Model):
    id = models.AutoField(primary_key=True)
    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE, null=False)
    invoice_number = models.CharField(max_length=64, null=False)
    invoice_details = models.TextField(null=True)
    invoice_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    date_created = models.DateField(null=False)
    billing_date = models.DateField(null=False)
    date_paid = models.DateField(null=False)

    def __str__(self):
        return f"{self.id}"
    
#class Under_contract(models.Model):
#    id = models.AutoField(primary_key=True)
#    estate_id = models.IntegerField(null=False)
#    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE, null=False)

#    def __str__(self):
#        return f"Under contract {self.id}"