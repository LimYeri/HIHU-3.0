from django.urls import path
from .views import *

urlpatterns = [
    # 식당 리스트
    path("List/", restaurantList.as_view(), name = "restaurantList"),
    # 식당 상세 페이지
    path("<int:pk>/", restaurantDetail.as_view(), name = "restaurantDetail"),
    # 오늘의 식당
    path("today", todayRestaurant, name = "todayRestaurant"),
]