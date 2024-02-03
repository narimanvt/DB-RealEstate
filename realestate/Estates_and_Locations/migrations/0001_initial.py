# Generated by Django 5.0.1 on 2024-02-03 11:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Clients_and_Contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Estate_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estate_status_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Estate_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=128)),
                ('country_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Estates_and_Locations.country')),
            ],
        ),
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estate_name', models.CharField(max_length=255, null=True)),
                ('floor_space', models.DecimalField(decimal_places=2, max_digits=8)),
                ('number_of_balconies', models.IntegerField()),
                ('balconies_space', models.DecimalField(decimal_places=2, max_digits=8)),
                ('number_of_bedrooms', models.IntegerField()),
                ('number_of_bathrooms', models.IntegerField()),
                ('number_of_garages', models.IntegerField()),
                ('number_of_parking_spaces', models.IntegerField()),
                ('pets_allowed', models.BooleanField()),
                ('has_elevator', models.BooleanField()),
                ('has_warehouse', models.BooleanField()),
                ('year_of_construction', models.IntegerField()),
                ('description', models.TextField(null=True)),
                ('state', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255, null=True)),
                ('street', models.CharField(max_length=255)),
                ('floor_number', models.IntegerField(default=1)),
                ('unit_number', models.IntegerField()),
                ('plate_number', models.CharField(max_length=10)),
                ('zip_code', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to='images/')),
                ('city', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Estates_and_Locations.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Estates_and_Locations.country')),
                ('estate_status_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Estates_and_Locations.estate_status')),
                ('estate_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Estates_and_Locations.estate_type')),
            ],
        ),
        migrations.CreateModel(
            name='In_charge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField()),
                ('data_to', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clients_and_Contacts.employee')),
                ('estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Estates_and_Locations.estate')),
            ],
        ),
    ]
