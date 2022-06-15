from rest_framework import serializers
from .models import Shedule


class SheduleSerializer(serializers.ModelSerializer):
    class Meta():
        model = Shedule
        fields = '__all__'

