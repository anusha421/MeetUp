# Generated by Django 4.0.1 on 2022-09-03 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0002_rename_owner_slots_admin_remove_slots_meeter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
