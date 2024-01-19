from django.contrib import admin
from .models import (
    Transaction,
    Contract_type,
    Contract,
    Contract_invoice,
)

# Register models with the custom admin classes

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('Transaction Type', 'Client Offered', 'Client Requested', 'Transaction Date')
    list_filter = ('Transaction Type', 'Transaction Date')
    search_fields = ['Transaction Type', 'Client Offered', 'Client Requested', 'Transaction Date']

@admin.register(Contract_type)
class ContractTypeAdmin(admin.ModelAdmin):
    list_display = ('Contract Type', )
    search_fields = ['Contract Type']

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('Client_id', 'Employee_id', 'Estate_id', 'Contract Type', 'Payment Amount', 'Start Date', 'End Date')
    list_filter = ('Contract Type', 'Start Date', 'End Date')
    search_fields = ['Contract Type']

@admin.register(Contract_invoice)
class ContractInvoiceAdmin(admin.ModelAdmin):
    list_display = ('Contract_id', 'Amount', 'Date Created', 'Billing Date', 'Date Paid')
    list_filter = ('Contract_id', 'Date Created', 'Billing Date', 'Date Paid')
    search_fields = ['Contract_id']

#admin.site.register(Transaction_type)
#admin.site.register(Transaction)
#admin.site.register(Payment_frequency)
#admin.site.register(Contract_type)
#admin.site.register(Contract)
#admin.site.register(Contract_invoice)
#admin.site.register(Under_contract)
