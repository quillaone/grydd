from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.company.models import Company


# Create your models here.
class Role(models.Model):
    name_role = models.CharField(max_length=130, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=False)

    class Meta:
        db_table = 'grydd_role'


class User(AbstractUser):
    email = models.EmailField(max_length=254, null=False, blank=False, unique=True)
    password = models.CharField(max_length=256, null=False)
    username = models.CharField(max_length=130, null=True, blank=False, unique=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=False, related_name="user")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']


class Employee(models.Model):
    name = models.CharField(max_length=100, null=True, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    password = models.CharField(max_length=256, null=True, blank=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="employee", null=True, blank=False)

    class Meta:
        db_table = 'grydd_employee'
