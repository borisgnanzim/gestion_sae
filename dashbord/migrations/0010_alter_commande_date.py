# Generated by Django 4.1.7 on 2023-03-16 15:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashbord', '0009_rename_client_commande_commande_client_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commande',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 3, 16, 15, 22, 33, 875585)),
        ),
    ]