# Generated by Django 4.1.7 on 2023-03-17 08:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashbord', '0014_rename_commande_attribution_attribution_commande_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribution',
            name='commande',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashbord.commande', unique=True),
        ),
        migrations.AlterField(
            model_name='commande',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 3, 17, 8, 3, 41, 798454)),
        ),
    ]
