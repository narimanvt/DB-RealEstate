from django.db import models

### Estates and Locations ###

class Estate_type(models.Model):
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=128, null=False)

    def __str__(self):
        return f"{self.type_name}"
    

class Estate_status(models.Model):
    id = models.AutoField(primary_key=True)
    estate_status_name = models.CharField(max_length=64, null=False)     

    def __str__(self):
        return f"{self.estate_status_name}"


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=128, null=False)

    def __str__(self):
        return f"{self.country_name}"


class City(models.Model):
    id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=128, null=False)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"{self.city_name}"
    

class Estate(models.Model):
    id = models.AutoField(primary_key=True)
    estate_name = models.CharField(max_length=255, null=True)
    city_id = models.IntegerField(null=False)
    estate_type_id = models.IntegerField(null=False)
    floor_space = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    number_of_balconies = models.IntegerField(null=False)
    balconies_space = models.DecimalField(max_digits=8, decimal_places=2, null=False)
    number_of_bedrooms = models.IntegerField(null=False)
    number_of_bathrooms = models.IntegerField(null=False)
    number_of_garages = models.IntegerField(null=False)
    number_of_parking_spaces = models.IntegerField(null=False)
    pets_allowed = models.BooleanField(null=False)
    has_elevator = models.BooleanField(null=False)
    has_warehouse = models.BooleanField(null=False)
    year_of_construction = models.IntegerField(null=False)
    estate_description = models.TextField(null=True)
    estate_status_id = models.IntegerField(null=False) 
    address = models.CharField(max_length=255, null=False)
    plate = models.IntegerField(null=False)
    zip_code = models.IntegerField(null=False)
    photo = models.ImageField(upload_to='images/', null=False)
    city_id = models.ForeignKey(City , on_delete=models.CASCADE, null=False)
    estate_type_id = models.ForeignKey(Estate_type, on_delete=models.CASCADE, null=False)
    estate_status_id = models.ForeignKey(Estate_status, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f"estate id {self.id}"


class In_charge(models.Model):
    id = models.AutoField(primary_key=True)
    estate_id = models.IntegerField(null=False)
    employee_id = models.IntegerField(null=False) 
    date_from = models.DateField(null=False)
    data_to = models.DateField(null=False)
    estate_id = models.ForeignKey(Estate, on_delete=models.CASCADE, null=False)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False)

    def __str__(self):
       return f"in_charge with id {self.id}"
