# Generated by Django 4.0.3 on 2022-04-04 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DelightsApp', '0004_remove_menuitems_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reciperequirement',
            name='slug',
        ),
    ]