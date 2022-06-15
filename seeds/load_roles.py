import sys, os, django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "grydd.settings")
django.setup()

from apps.users.models import Role
from rest_framework import status
from rest_framework.response import Response
from environs import Env
import datetime

now = datetime.datetime.now()

def load_roles():
    roles = [
        {
            "name_role": "Admin Application",
            "description": "Admin Application",
            "created_at": now},
        {
            "name_role": "Admin Company",
            "description": "Admin Company",
            "created_at": now},
        {
            "name_role": "Employee",
            "description": "Employee",
            "created_at": now}

    ]
    for role in roles:
        Role.objects.create(**role)
    return Response({"success"})


load_roles()
