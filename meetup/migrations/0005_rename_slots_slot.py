# Generated by Django 4.0.1 on 2022-09-03 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0004_rename_name_user_fullname'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Slots',
            new_name='Slot',
        ),
    ]
