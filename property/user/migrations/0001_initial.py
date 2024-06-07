# Generated by Django 5.0.6 on 2024-06-06 12:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('input', '0007_location_total_visits'),
    ]

    operations = [
        migrations.CreateModel(
            name='enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=11)),
                ('info', models.CharField(max_length=250)),
                ('property_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='input.location')),
            ],
        ),
    ]