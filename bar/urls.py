from django.urls import path
from .views import *

urlpatterns = [
    # 주점 리스트
    path("List/", barList.as_view(), name = "barList"),
    # 주점 상세 페이지
    path("<int:pk>/", barDetail.as_view(), name = "barDetail"),
    # 오늘의 주점
    path("today", todayBar, name = "todayBar"),
]