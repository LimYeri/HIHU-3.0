from django.urls import path
from main.views import *

urlpatterns = [
    # 메인 페이지
    path("", index, name = "index"),
    # About 페이지
    path("about/", about, name = "about"),
    # 버스 시간표
    path("busTime/", busTime, name = "busTime"),
    # 오늘 뭐먹지
    path("todayShop/", todayShop, name = "todayShop"),
    path("ads.txt", ads),
    # 검색 페이지
    path("totalSearch/", totalSearch, name = "totalSearch"),
]