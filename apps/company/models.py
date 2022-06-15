from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Company(models.Model):
    administered_user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="company")
    nit = models.CharField(max_length=50, null=False, blank=False, unique=True)
    name_company = models.CharField(max_length=100, null=False, blank=False, unique=True)
    trade_name = models.CharField(max_length=100, null=True, blank=False)
    address = models.CharField(max_length=100, null=True, blank=False)
    phone = models.CharField(max_length=50, null=True, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False, unique=True)
    web_site = models.URLField(max_length=200, null=True, blank=False)
    country = models.CharField(max_length=100, null=True, blank=False)
    city = models.CharField(max_length=100, null=True, blank=False)
    description = models.TextField(null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'grydd_company'
