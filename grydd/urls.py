from django.contrib import admin
from django.urls import re_path, include

urlpatterns = [
    re_path('admin', admin.site.urls),
    re_path('grydd/', include('apps.users.urls')),
    re_path('grydd/', include('apps.company.urls')),
    re_path('grydd/', include('apps.access_point.urls')),
    re_path('grydd/', include('apps.shedule.urls')),
]
