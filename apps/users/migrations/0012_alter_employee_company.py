# Generated by Django 4.0.5 on 2022-06-15 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_alter_company_administered_user'),
        ('users', '0011_alter_employee_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='company.company'),
        ),
    ]
