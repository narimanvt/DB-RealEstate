from django.urls import path
from . import views

app_name = "Estates_and_Locations"
urlpatterns = [
    path('', views.main_page, name="main_page"),
    path('options/', views.options, name="options"),
    path('property/', views.property, name="property"),
]