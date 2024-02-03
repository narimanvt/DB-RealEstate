# Generated by Django 5.0.1 on 2024-02-03 11:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Clients_and_Contacts', '0001_initial'),
        ('Estates_and_Locations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='estate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Estates_and_Locations.estate'),
        ),
        migrations.AddField(
            model_name='contact',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clients_and_Contacts.employee'),
        ),
    ]