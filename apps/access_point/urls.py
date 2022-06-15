from django.urls import path
from .views import AccessPointCompanyListView, AccessPointCompanyDetailView, StatusListView, StatusDetailView

urlpatterns = [
    path('access_point_company/', AccessPointCompanyListView.as_view()),  # GET, POST
    path('access_point_company/<int:pk>/', AccessPointCompanyDetailView.as_view()),  # GET, PUT, DELETE
    path('status/', StatusListView.as_view()),  # GET, POST
    path('status/<int:pk>/', StatusDetailView.as_view()),  # GET, PUT, DELETE
]
