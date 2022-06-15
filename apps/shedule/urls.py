from django.urls import path
from .views import SheduleListView, SheduleDetailView


urlpatterns = [
    path('shedule/', SheduleListView.as_view()),
    path('shedule/<int:pk>/', SheduleDetailView.as_view())
]
