# Generated by Django 4.2.3 on 2023-11-21 02:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0003_alter_menu_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='name',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='inventory',
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_slot',
            field=models.SmallIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='menu_item_descprtion',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
