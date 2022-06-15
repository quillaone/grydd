from django.db import models
from apps.users.models import User


# Create your models here.
class Shedule(models.Model):
    name_shedule = models.CharField(max_length=130, null=False, blank=False)
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False, related_name="shedule")
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=False)

    class Meta:
        db_table = 'grydd_shedule'
