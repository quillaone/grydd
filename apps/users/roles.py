from .models import Role, User
from .serializers import UserRoleSerializer, UserSerializer
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
import django_auto_prefetching
from django_auto_prefetching import AutoPrefetchViewSetMixin


class RolesListView(APIView, LimitOffsetPagination, AutoPrefetchViewSetMixin):
    serializer_class = UserRoleSerializer

    def get(self, request):
        roles = Role.objects.all()
        paginator = LimitOffsetPagination()
        page = paginator.paginate_queryset(roles, request)
        serializer = UserRoleSerializer(page, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserRoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoleDetailView(APIView):
    def get(self, request, pk=None):
        try:
            role = Role.objects.filter(pk=pk)
            if role.exists():
                role = role.select_related()
                serializer = UserRoleSerializer(role, many=True)
                return Response(serializer.data)
            return Response({"Role not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        try:
            role = Role.objects.filter(pk=pk)
            if role.exists():
                serializer = UserRoleSerializer(role, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"Role not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        try:
            role = Role.objects.filter(pk=pk)
            if role.exists():
                role.delete()
                return Response({"Role deleted"}, status=status.HTTP_204_NO_CONTENT)
            return Response({"Role not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


