# Generated by Django 4.2.3 on 2023-11-21 02:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_alter_booking_booking_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booking_slot',
        ),
    ]
