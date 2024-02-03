from django.urls import path
from Clients_and_Contacts import views

app_name = "Clients_and_Contacts"
urlpatterns = [
    path('', views.Clients_and_Contacts, name="Clients_and_Contacts"),
    path("sign_in", views.sign_in_request, name="sign_in")
]