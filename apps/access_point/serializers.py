from rest_framework import serializers
from .models import AccessPointCompany, Status


class AccessPointCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = AccessPointCompany
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    access_point_company = AccessPointCompanySerializer(read_only=True, many=True)
    class Meta:
        model = Status
        fields = '__all__'
