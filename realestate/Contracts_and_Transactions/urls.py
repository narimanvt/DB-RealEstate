from django.urls import path
from . import views

app_name = "Contracts_and_Transactions"
urlpatterns = [
    path('contracts/', views.contract_list, name="contract_list"),
    path('transactions/', views.transaction_list, name="transaction_list"),
]
