# Generated by Django 4.0.1 on 2022-09-03 11:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slots',
            old_name='owner',
            new_name='admin',
        ),
        migrations.RemoveField(
            model_name='slots',
            name='meeter',
        ),
        migrations.AddField(
            model_name='slots',
            name='public',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='meeter', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
