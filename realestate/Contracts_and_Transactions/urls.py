from django.urls import path
from . import views

app_name = "Contracts_and_Transactions"
urlpatterns = [
    path('', views.Contracts_and_Transactions, name="Contracts_and_Transactions")
]