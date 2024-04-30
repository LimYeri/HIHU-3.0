from django.shortcuts import render, redirect
from django.views.generic import ListView
from schedule.models import Schedule
from django.db.models import Q

from django.core import serializers
from django.http import JsonResponse
from datetime import datetime

from django.template.loader import render_to_string

import json

# 일정 (AJAX)
def ScheduleHIHU(request):
    if request.method == 'POST':
        this_month = request.POST['month']
        # 해당 월에 시작일 또는 종료일이 있는 학사일정을 가져와 시작일을 기준으로 오름차순으로 정렬
        schedule = Schedule.objects.filter(Q(startDate__month=this_month) | Q(endDate__month=this_month)).order_by('startDate')
        # 학사일정을 JSON 형식으로 직렬화
        schedule_json = json.loads(serializers.serialize('json', schedule, ensure_ascii=False))
        return JsonResponse({'Schedule_json': schedule_json}) # JSON 반환
    else:
        # 현재 월에 시작일 또는 종료일이 있는 학사일정을 가져와 시작일을 기준으로 오름차순으로 정렬
        schedule = Schedule.objects.filter(Q(startDate__month=datetime.now().month) | Q(endDate__month=datetime.now().month)).order_by('startDate')
        return render(request, 'calendar.html', {'Schedule_list': schedule, 'listcount': schedule.count()})