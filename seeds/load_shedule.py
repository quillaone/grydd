import sys, os, django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "grydd.settings")
django.setup()

from apps.shedule.models import Shedule
import datetime

def load_shedule():
    shedule = [

        {
            "name_shedule": "Tomorrow",
            "start_time": "07:00",
            "end_time": "13:00",
            "created_at": datetime.datetime.now()},
        {
            "name_shedule": "Afternoon",
            "start_time": "13:00",
            "end_time": "19:00",
            "created_at": datetime.datetime.now()},
        {
            "name_shedule": "Night",
            "start_time": "19:00",
            "end_time": "07:00",
            "created_at": datetime.datetime.now()}

    ]
    for shedule in shedule:
        Shedule.objects.create(**shedule)
    print("Shedule loaded")
    return "success"

load_shedule()
