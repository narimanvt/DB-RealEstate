from django.contrib import admin
from .models import (
    Transaction_type,
    Transaction,
    Contract_type,
    Payment_frequency,
    Contract,
    Contract_invoice,
    Under_contract,
)

# Register models with the custom admin classes
@admin.register(Transaction_type)
class TransactionTypeAdmin(admin.ModelAdmin):
    list_display = ('transaction_type_name', )
    search_fields = ['transaction_type_name']

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_type', 'client_offered', 'client_requested', 'date')
    list_filter = ('transaction_type', 'date')
    search_fields = ['transaction_type', 'client_offered', 'client_requested', 'date']

@admin.register(Contract_type)
class ContractTypeAdmin(admin.ModelAdmin):
    list_display = ('contract_type', )
    search_fields = ['contract_type']

@admin.register(Payment_frequency)
class PaymentFrequencyAdmin(admin.ModelAdmin):
    list_display = ('payment_frequency_name', )
    search_fields = ['payment_frequency_name']

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('client', 'employee', 'estate', 'contract_type', 'payment_amount', 'start_date', 'end_date')
    list_filter = ('contract_type', 'start_date', 'end_date')
    search_fields = ['contract_type']

@admin.register(Contract_invoice)
class ContractInvoiceAdmin(admin.ModelAdmin):
    list_display = ('contract', 'invoice_amount', 'date_created', 'billing_date', 'date_paid')
    list_filter = ('contract', 'date_created', 'billing_date', 'date_paid')
    search_fields = ['contract']

@admin.register(Under_contract)
class UnderContractAdmin(admin.ModelAdmin):
    list_display = ('estate', 'contract')
    list_filter = ('estate', 'contract')
    search_fields = ['estate', 'contract']