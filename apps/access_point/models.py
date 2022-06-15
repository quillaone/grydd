from django.db import models
from apps.company.models import Company
from apps.shedule.models import Shedule


class Status(models.Model):
    name_status = models.CharField(max_length=130, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=False)

    class Meta:
        db_table = 'grydd_status_access_point'


class AccessPointCompany(models.Model):
    name_access_point = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="access_point_company")
    geo_location = models.CharField(max_length=100, null=True, blank=False)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="access_point_company")
    shedule = models.ForeignKey(Shedule, on_delete=models.CASCADE)

    class Meta:
        db_table = 'grydd_access_point_company'
