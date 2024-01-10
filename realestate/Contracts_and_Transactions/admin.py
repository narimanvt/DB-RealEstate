from django.contrib import admin
from .models import Transaction_type, Transaction, Payment_frequency, Contract_type, Contract, Contract_invoice, Under_contract

# Register your models here.

admin.site.register(Transaction_type)
admin.site.register(Transaction)
admin.site.register(Payment_frequency)
admin.site.register(Contract_type)
admin.site.register(Contract)
admin.site.register(Contract_invoice)
admin.site.register(Under_contract)