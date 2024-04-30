from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from club.models import Club

class clubList(ListView):
    model = Club
    ordering = 'name' # 동아리 이름 기준 내림차순 정렬
    context_object_name = 'club_list'
    template_name = 'clubList.html'
    paginate_by = 5

class clubDetail(DetailView):
    model = Club
    ordering = 'name'
    context_object_name = 'clubDetail'
    template_name = 'clubDetail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clubList'] = Club.objects.all().order_by('name')
        return context