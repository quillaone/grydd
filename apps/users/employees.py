from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EmployeeSerializer
from rest_framework.pagination import LimitOffsetPagination
import django_auto_prefetching
from django_auto_prefetching import AutoPrefetchViewSetMixin
from .models import Employee
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
class EmployeeListView(APIView, LimitOffsetPagination, AutoPrefetchViewSetMixin):
    serializer_class = EmployeeSerializer

    def get(self, request):
        try:
            employees = Employee.objects.all()
            employees = employees.select_related()
            self.paginate_queryset(employees, request, view=self)
            results = django_auto_prefetching.prefetch(employees, self.serializer_class)
            serializer = EmployeeSerializer(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as error:
            datos = {'message': str(error)}
            return Response(datos, status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        serializers = EmployeeSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            datos = {'message': "success created",
                     'result': serializers.data}
            return Response(datos, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetailView(APIView, LimitOffsetPagination, AutoPrefetchViewSetMixin):
    serializer_class = EmployeeSerializer

    def get(self, request, pk=None):
        try:
            employee = Employee.objects.filter(id=pk)
            employee = employee.select_related()
            self.paginate_queryset(employee, request, view=self)
            results = django_auto_prefetching.prefetch(employee, self.serializer_class)
            serializer = EmployeeSerializer(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as error:
            return Response({'message': str(error)}, status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk=None):
        employee = Employee.objects.get(id=pk)
        serializers = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            datos = {'message': "success updated",
                     'result': serializers.data}
            return Response(datos, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            employee = Employee.objects.get(id=pk)
            employee.delete()
            datos = {'message': "success deleted"}
            return Response(datos, status=status.HTTP_200_OK)
        except Exception as error:
            return Response({'message': str(error)}, status=status.HTTP_400_BAD_REQUEST)


def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['juanjo0216@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/success/')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')
