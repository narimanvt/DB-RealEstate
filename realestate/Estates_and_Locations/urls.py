from django.urls import path
from . import views

app_name = "Estates_and_Locations"
urlpatterns = [
    path('', views.main_page, name="main_page"),
    path('estate_form/', views.estate_form, name="estate_form"),
    path('property/', views.property, name="property"),
    path('details/', views.details, name="details")
]