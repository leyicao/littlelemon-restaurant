# Generated by Django 4.2.3 on 2023-07-12 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='no_of_guest',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
