# Generated by Django 4.0.3 on 2022-04-10 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MessageBoard', '0006_remove_message_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='userid',
            new_name='user',
        ),
    ]
