from django.urls import path
from . import views

app_name = "Clients_and_Contacts"
urlpatterns = [
    path('', views.Clients_and_Contacts, name="Clients_and_Contacts"),
    path("register", views.register_request, name="register")
]