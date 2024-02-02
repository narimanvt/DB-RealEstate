from django.db import models
import datetime

class Country(models.Model):
    country_name = models.CharField(max_length=128, null=False)

    def __str__(self):
        return f"{self.country_name}"


class City(models.Model):
    city_name = models.CharField(max_length=128, null=False)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"{self.city_name}"


class Address(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    street_number = models.IntegerField()
    building_name = models.CharField(max_length=255, blank=True)
    district = models.CharField(max_length=255)
    floor = models.IntegerField()
    unit_number = models.IntegerField()
    plate_number = models.CharField(max_length=10)
    zip_code = models.CharField(max_length=20)

class Estate_type(models.Model):

    ESTATE_TYPES = (
        ("Apartment", "Apartment"),
        ("House", "House"),
        ("Office", "Office"),
        ("Villa", "Villa"),
        ("Retail", "Retail"),
        ("Land", "Land"),
        ("Warehouse", "Warehouse"),
        ("Industrial Shed", "Industrial Shed"),
        ("PentHouse", "PentHouse")
    )
    type_name = models.CharField(max_length=15, null=False, unique=True, choices=ESTATE_TYPES)

    def __str__(self):
        return f"{self.type_name}"
    

class Estate_status(models.Model):
    estate_status_name = models.CharField(max_length=64, null=False)     

    def __str__(self):
        return f"{self.estate_status_name}"


class Estate(models.Model):
    estate_name = models.CharField(max_length=255, null=True)
    estate_type_id = models.ForeignKey(Estate_type, on_delete=models.CASCADE, null=False)
    estate_status_id = models.ForeignKey(Estate_status, on_delete=models.CASCADE, null=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=False)
    floor_space = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    number_of_balconies = models.IntegerField(null=False)
    balconies_space = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    number_of_bedrooms = models.IntegerField(null=False)
    number_of_bathrooms = models.IntegerField(null=False)
    number_of_garages = models.IntegerField(null=False)
    number_of_parking_spaces = models.IntegerField(null=False)
    is_pets_allowed = models.BooleanField(null=False)
    has_elevator = models.BooleanField(null=False)
    has_warehouse = models.BooleanField(null=False)
    year_of_construction = models.IntegerField(null=False)
    description = models.TextField(null=True)
    photo = models.ImageField(upload_to='images/', null=False)

    def get_age_of_construction(self):
        current_year = datetime.datetime.now().year
        year_of_construction = self.year_of_construction
        return current_year - year_of_construction

    def __str__(self):
        return f"estate id {self.id}"


class In_charge(models.Model):
    date_from = models.DateField(null=False)
    data_to = models.DateField(null=False)
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE, null=False)
    employee = models.ForeignKey('Clients_and_Contacts.Employee', on_delete=models.CASCADE, null=False)

    def __str__(self):
       return f"in_charge with id {self.id}"