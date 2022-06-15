import django_auto_prefetching
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from django_auto_prefetching import AutoPrefetchViewSetMixin
from .models import Shedule
from .serializers import SheduleSerializer


class SheduleListView(APIView, LimitOffsetPagination, AutoPrefetchViewSetMixin):
    serializer_class = SheduleSerializer

    def get(self, request):
        try:
            shedule = Shedule.objects.all()
            shedule = shedule.select_related()
            self.paginate_queryset(shedule, request, view=self)
            results = django_auto_prefetching.prefetch(shedule, self.serializer_class)
            serializer = SheduleSerializer(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = SheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SheduleDetailView(APIView):

    def get(self, request, pk=None):
        try:
            shedule = Shedule.objects.filter(pk=pk)
            if shedule.exists():
                shedule = shedule.select_related()
                serializer = SheduleSerializer(shedule, many=True)
                return Response(serializer.data)
            return Response({"Shedule not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        shedule = Shedule.objects.filter(pk=pk).first()
        if shedule:
            serializer = SheduleSerializer(shedule, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"Shedule not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        try:
            shedule = Shedule.objects.filter(pk=pk)
            if shedule.exists():
                shedule.delete()
                return Response({"Shedule deleted"}, status=status.HTTP_204_NO_CONTENT)
            return Response({"Shedule not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
