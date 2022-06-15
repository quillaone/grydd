from rest_framework import serializers
from .models import Company
from apps.access_point.serializers import AccessPointCompanySerializer

class CompanySerializer(serializers.ModelSerializer):
    access_point_company = AccessPointCompanySerializer(read_only=True, many=True)

    class Meta():
        model = Company
        fields = '__all__'
