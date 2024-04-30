from django.urls import path
from .views import *

urlpatterns = [
    # HIHU 학사일정
    path("", ScheduleHIHU, name = "ScheduleHIHU"),
]