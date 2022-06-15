import django_auto_prefetching
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from django_auto_prefetching import AutoPrefetchViewSetMixin
from .models import Company
from .serializers import CompanySerializer


class CompanyListView(APIView, LimitOffsetPagination, AutoPrefetchViewSetMixin):
    serializer_class = CompanySerializer

    def get(self, request):
        try:
            companies = Company.objects.all()
            companies = companies.select_related()
            self.paginate_queryset(companies, request, view=self)
            results = django_auto_prefetching.prefetch(companies, self.serializer_class)
            serializer = CompanySerializer(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyDetailView(APIView):

    def get(self, request, pk=None):
        try:
            company = Company.objects.filter(pk=pk)
            if company.exists():
                company = company.select_related()
                serializer = CompanySerializer(company, many=True)
                return Response(serializer.data)
            return Response({"Company not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        try:
            company = Company.objects.filter(pk=pk)
            if company.exists():
                serializer = CompanySerializer(company, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"Company not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            company = Company.objects.filter(pk=pk)
            if company.exists():
                company.delete()
                return Response({"Company deleted"}, status=status.HTTP_204_NO_CONTENT)
            return Response({"Company not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
