# Generated by Django 4.0.3 on 2022-04-10 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MessageBoard', '0005_alter_message_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
    ]
