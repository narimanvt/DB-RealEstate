from django.db import models

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ("Buy", "Buy"),
        ("Rent", "Rent"),
        ("Barter", "Barter"),
        ("Mortgage", "Mortgage"),
        ("Pre-Sale", "Pre-Sale")
        ("Lease And Rent", "Lease And Rent"),
    )
    transaction_type = models.CharField(max_length=128, null=False, choices=TRANSACTION_TYPES.choices)
    client_offered = models.ForeignKey('Clients_and_Contacts.Client', on_delete=models.CASCADE, related_name='offered_transactions', null=False)
    client_requested = models.ForeignKey('Clients_and_Contacts.Client', on_delete=models.CASCADE, related_name='requested_transactions', null=False) 
    date = models.DateField(null=False)
    details = models.TextField(null=True)

    def __str__(self):
        return f"Transaction with id {self.id}"


class Contract_type(models.Model):
    contract_type = models.CharField(max_length=64, null=False)
    fee_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=False)

    def __str__(self):
        return f"{self.contract_type_name}"


class Contract(models.Model):
    client = models.ForeignKey('Clients_and_Contacts.Client', on_delete=models.CASCADE, null=False)
    employee = models.ForeignKey('Clients_and_Contacts.Employee', on_delete=models.CASCADE, null=False)
    estate = models.ForeignKey('Estates_and_Locations.Estate', null=False)
    transaction_id = models.ForeignKey(Transaction, on_delete=models.CASCADE, null=False)
    contract_type = models.ForeignKey(Contract_type, on_delete=models.CASCADE, null=False)
    details = models.TextField(null=True)
    number_of_invoices = models.IntegerField(null=False)
    payment_frequency = models.CharField(max_length=64, null=False)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    fee_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    fee_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    date_signed = models.DateField(null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)

    def __str__(self) :
        return f"Contract with id {self.id}"


class Contract_invoice(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, null=False)
    invoice_number = models.CharField(max_length=64, null=False)
    invoice_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    details = models.TextField(null=True)
    date_created = models.DateField(null=False)
    billing_date = models.DateField(null=False)
    date_paid = models.DateField(null=False)

    def __str__(self):
        return f"{self.id}"