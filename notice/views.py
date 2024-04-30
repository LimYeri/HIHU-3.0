from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from notice.models import Post

class noticeList(ListView):
    model = Post
    ordering = '-pk' # 공지사항 최신순 정렬
    template_name = 'noticeList.html'
    paginate_by = 8

class noticePostDetail(DetailView):
    model = Post
    ordering = 'pk'
    context_object_name = 'noticePost'
    template_name = 'noticePostDetail.html'