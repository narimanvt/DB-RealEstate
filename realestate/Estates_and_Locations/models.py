from django.db import models
from Clients_and_Contacts.models import Employee

### Estates and Locations ###

#class Estate_type(models.Model):
#    id = models.AutoField(primary_key=True)
#    type_name = models.CharField(max_length=128, null=False)

#    def __str__(self):
#        return f"{self.type_name}"


#class Estate_status(models.Model):
#    id = models.AutoField(primary_key=True)
#    estate_status_name = models.CharField(max_length=64, null=False)     

#    def __str__(self):
#        return f"{self.estate_status_name}"


#class Country(models.Model):
#    id = models.AutoField(primary_key=True)
#    country_name = models.CharField(max_length=128, null=False)

#    def __str__(self):
#        return f"{self.country_name}"


#class City(models.Model):
#    id = models.AutoField(primary_key=True)
#    city_name = models.CharField(max_length=128, null=False)
#    country_id = models.ForeignKey(Country, on_delete=models.CASCADE, null=False)

#    def __str__(self):
#        return f"{self.city_name}"
    

class Address(models.Model):

    CITY_NAME = ()




    
    State = models.CharField(max_length=255) 
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    street_number = models.IntegerField()
    building_name = models.CharField(max_length=255, blank=True)
    district = models.CharField(max_length=255)
    floor = models.IntegerField()
    unit_number = models.IntegerField()
    plate_number = models.CharField(max_length=10)
    zip_code = models.CharField(max_length=20)
    coordinate = models.CharField(max_length=255)
    

class Estate(models.Model):

    ESTATE_TYPES = (
        ("Apartment", "Apartment"),
        ("House", "House"),
        ("Office", "Office"),
        ("Villa", "Villa"),
        ("Retail", "Retail")
        ("Land", "Land"),
        ("Warehouse", "Warehouse"),
        ("Industrial Shed", "Industrial Shed"),
        ("PentHouse", "PentHouse")
    )

    PETS_ALLOWED_TYPES = (
        ("Yes", "Yes"),
        ("No", "No")
    )

    HAS_ELEVATOR_TYPES = (
        ("Yes", "Yes"),
        ("No", "No")
    )


    HAS_WAREHOUSE_TYPES = (
        ("Yes", "Yes"),
        ("No", "No")
    )

    id = models.AutoField(primary_key=True)
    estate_name = models.CharField(max_length=255, null=True)
    estate_type = models.CharField(max_length=128, null=False, choices=ESTATE_TYPES.choices)
    floor_space = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    number_of_balconies = models.IntegerField(null=False)
    balconies_space = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    number_of_bedrooms = models.IntegerField(null=False)
    number_of_bathrooms = models.IntegerField(null=False)
    number_of_garages = models.IntegerField(null=False)
    number_of_parking_spaces = models.IntegerField(null=False)
    pets_allowed = models.BooleanField(null=False, choices=PETS_ALLOWED_TYPES.choices)
    has_elevator = models.BooleanField(null=False, choices=HAS_ELEVATOR_TYPES.choices)
    has_warehouse = models.BooleanField(null=False, choices=HAS_WAREHOUSE_TYPES.choices)
    year_of_construction = models.IntegerField(null=False)
    estate_description = models.TextField(null=True)
    estate_status_id = models.IntegerField(null=False) 
    photo = models.ImageField(upload_to='images/', null=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"estate id {self.id}"


class In_charge(models.Model):
    id = models.AutoField(primary_key=True)
    date_from = models.DateField(null=False)
    data_to = models.DateField(null=False)
    estate_id = models.ForeignKey(Estate, on_delete=models.CASCADE, null=False)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False)

    def __str__(self):
       return f"in_charge with id {self.id}"
