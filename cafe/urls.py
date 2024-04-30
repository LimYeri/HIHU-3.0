from django.urls import path
from .views import *

urlpatterns = [
    # 카페 리스트
    path("List/", cafeList.as_view(), name = "cafeList"),
    # 카페 상세 페이지
    path("<int:pk>/", cafeDetail.as_view(), name = "cafeDetail"),
    # 오늘의 카페
    path("today", todayCafe, name = "todayCafe"),
]