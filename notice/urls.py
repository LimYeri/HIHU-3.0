from django.urls import path
from .views import *

urlpatterns = [
    # 공지사항 리스트
    path("List/", noticeList.as_view(), name = "noticeList"),
    # 공지사항 상세 페이지
    path("<int:pk>/", noticePostDetail.as_view(), name = "noticePostDetail"),
]