# Generated by Django 4.0.5 on 2022-06-14 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_employee_password_alter_role_name_role_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='password',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=256),
        ),
    ]
