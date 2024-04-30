from django.urls import path
from .views import *

urlpatterns = [
    # 동아리 리스트
    path("List/", clubList.as_view(), name = "clubList"),
    # 동아리 상세 페이지
    path("<int:pk>/", clubDetail.as_view(), name = "clubDetail"),
]