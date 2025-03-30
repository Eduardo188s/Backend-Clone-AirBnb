# Generated by Django 5.0.1 on 2025-03-28 23:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_rename_landlor_property_landlord_reservation'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='favorited',
            field=models.ManyToManyField(blank=True, related_name='favorites', to=settings.AUTH_USER_MODEL),
        ),
    ]
