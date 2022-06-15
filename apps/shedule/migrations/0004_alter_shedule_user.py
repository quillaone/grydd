# Generated by Django 4.0.5 on 2022-06-15 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shedule', '0003_alter_shedule_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shedule',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shedule', to=settings.AUTH_USER_MODEL),
        ),
    ]