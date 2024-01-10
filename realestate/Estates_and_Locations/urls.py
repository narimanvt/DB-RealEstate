from django.urls import path
from . import views

app_name = "Estates_and_Locations"
urlpatterns = [
    path('', views.app, name="Estates_and_Locations")
]