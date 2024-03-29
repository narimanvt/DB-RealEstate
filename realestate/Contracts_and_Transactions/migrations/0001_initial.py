# Generated by Django 5.0.1 on 2024-02-03 11:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Clients_and_Contacts', '0002_initial'),
        ('Estates_and_Locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_type', models.CharField(max_length=64)),
                ('fee_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Payment_frequency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_frequency_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField(null=True)),
                ('number_of_invoices', models.IntegerField()),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fee_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fee_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_signed', models.DateField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clients_and_Contacts.client')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clients_and_Contacts.employee')),
                ('estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Estates_and_Locations.estate')),
                ('contract_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Contracts_and_Transactions.contract_type')),
                ('payment_frequency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Contracts_and_Transactions.payment_frequency')),
            ],
        ),
        migrations.CreateModel(
            name='Contract_invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(max_length=64)),
                ('invoice_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('details', models.TextField(null=True)),
                ('date_created', models.DateField()),
                ('billing_date', models.DateField()),
                ('date_paid', models.DateField()),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Contracts_and_Transactions.contract')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('details', models.TextField(null=True)),
                ('client_offered', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offered_transactions', to='Clients_and_Contacts.client')),
                ('client_requested', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requested_transactions', to='Clients_and_Contacts.client')),
                ('transaction_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Contracts_and_Transactions.transaction_type')),
            ],
        ),
        migrations.AddField(
            model_name='contract',
            name='transaction_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Contracts_and_Transactions.transaction'),
        ),
        migrations.CreateModel(
            name='Under_contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Contracts_and_Transactions.contract')),
                ('estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Estates_and_Locations.estate')),
            ],
        ),
    ]
