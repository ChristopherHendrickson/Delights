# Generated by Django 4.0.3 on 2022-04-09 23:55

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MessageBoard', '0003_alter_message_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.CharField(default=django.contrib.auth.models.User, max_length=500),
        ),
    ]