import django_auto_prefetching
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from django_auto_prefetching import AutoPrefetchViewSetMixin
from .models import AccessPointCompany, Status
from .serializers import AccessPointCompanySerializer, StatusSerializer


class AccessPointCompanyListView(APIView, LimitOffsetPagination, AutoPrefetchViewSetMixin):
    serializer_class = AccessPointCompanySerializer

    def get(self, request):
        try:
            access_point_companies = AccessPointCompany.objects.all()
            access_point_companies = access_point_companies.select_related()
            self.paginate_queryset(access_point_companies, request, view=self)
            results = django_auto_prefetching.prefetch(access_point_companies, self.serializer_class)
            serializer = AccessPointCompanySerializer(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = AccessPointCompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccessPointCompanyDetailView(APIView):

    def get(self, request, pk=None):
        try:
            access_point_company = AccessPointCompany.objects.filter(pk=pk)
            if access_point_company.exists():
                access_point_company = access_point_company.select_related()
                serializer = AccessPointCompanySerializer(access_point_company, many=True)
                return Response(serializer.data)
            return Response({"AccessPointCompany not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        try:
            access_point_company = AccessPointCompany.objects.filter(pk=pk)
            if access_point_company.exists():
                serializer = AccessPointCompanySerializer(access_point_company, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"AccessPointCompany not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            access_point_company = AccessPointCompany.objects.filter(pk=pk)
            if access_point_company.exists():
                access_point_company.delete()
                return Response({"AccessPointCompany deleted"}, status=status.HTTP_204_NO_CONTENT)
            return Response({"AccessPointCompany not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


class StatusListView(APIView, LimitOffsetPagination, AutoPrefetchViewSetMixin):
    serializer_class = StatusSerializer

    def get(self, request):
        try:
            statuses = Status.objects.all()
            statuses = statuses.select_related()
            self.paginate_queryset(statuses, request, view=self)
            results = django_auto_prefetching.prefetch(statuses, self.serializer_class)
            serializer = StatusSerializer(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StatusDetailView(APIView):

    def get(self, request, pk=None):
        try:
            status = Status.objects.filter(pk=pk)
            if status.exists():
                status = status.select_related()
                serializer = StatusSerializer(status, many=True)
                return Response(serializer.data)
            return Response({"Status not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        try:
            status = Status.objects.filter(pk=pk).first()
            if status:
                serializer = StatusSerializer(status, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"Status not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            status = Status.objects.filter(pk=pk)
            if status.exists():
                status.delete()
                return Response({"Status deleted"}, status=status.HTTP_204_NO_CONTENT)
            return Response({"Status not found"}, 400)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
