from django.urls import path
from . import views

app_name = "Clients_and_Contacts"
urlpatterns = [
    path('clients/', views.client_list, name="client_list"),
    path('employees/', views.employee_list, name="employee_list"),
]
