# Generated by Django 5.0.2 on 2024-02-19 10:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_deliveryarea_kitchen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryarea',
            name='kitchen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_areas', to='dashboard.kitchen'),
        ),
    ]
