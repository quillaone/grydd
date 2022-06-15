from rest_framework import serializers
from .models import User, Role, Employee
from apps.company.serializers import CompanySerializer
from apps.shedule.serializers import SheduleSerializer
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core import mail


class UserSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True, many=True)
    shedule = SheduleSerializer(read_only=True, many=True)

    class Meta():
        model = User
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class UserRoleSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=True)

    class Meta():
        model = Role
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    role = UserRoleSerializer(read_only=True, many=True)

    class Meta():
        model = Employee
        fields = '__all__'

    def validate(self, data):
        if "company" in data:
            if Employee.objects.filter(company=data["company"], email=data["email"]).exists():
                raise serializers.ValidationError("This employee is already registered with this company.")
        return data

    # send email to employee when he is created
    def create(self, validated_data):
        with mail.get_connection() as connection:
            try:
                send_mail(
                    'Welcome to the company',
                    'You have been registered in the company' + " " + validated_data['company'].name_company,
                    settings.EMAIL_HOST_USER,
                    [validated_data['email']] if validated_data['email'] else [],
                    fail_silently=False,
                    connection=connection,
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        return super(EmployeeSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        with mail.get_connection() as connection:
            try:
                send_mail(
                    'Welcome to the company',
                    'You has updated your profile in the company',
                    settings.EMAIL_HOST_USER,
                    [validated_data['email']],
                    fail_silently=False,
                    connection=connection,
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        return super(EmployeeSerializer, self).update(instance, validated_data)
