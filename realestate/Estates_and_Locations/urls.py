from django.urls import path
from . import views

app_name = "Estates_and_Locations"
urlpatterns = [
    path('', views.Estates_and_Locations, name="Estates_and_Locations")
]