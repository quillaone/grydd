# Generated by Django 4.0.5 on 2022-06-15 06:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shedule', '0002_shedule_name_shedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shedule',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
