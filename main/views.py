from django.shortcuts import render

from schedule.models import Schedule
from notice.models import Post
from .models import Banner, VisitorCount

from django.http import HttpResponse

from django.db.models import Sum

from datetime import datetime
from django.db.models import Q

from cafe.models import Cafe, CafeMenu
from bar.models import Bar, BarMenu
from restaurant.models import Restaurant, RestaurantMenu

# 메인 페이지
def index(request):
    now = datetime.now()
    # 오늘 날짜 기준 가장 가까운 학사 일정 2개
    now_event = Schedule.objects.filter(Q(startDate__lte=now) & Q(endDate__gte=now)).order_by('startDate')[:1]
    recent_notice = Post.objects.last()   
    Banners = Banner.objects.all().order_by('id') 
    
    if now_event :
        # 오늘에 걸친 이벤트가 있으면
        events = Schedule.objects.filter(Q(startDate__gte=now_event[0].startDate) & Q(endDate__gte=now)).order_by('startDate')[:2]
    else :
        events = Schedule.objects.filter(startDate__gte=now).order_by('startDate')[:2]
    # response = render(request, "index.html", {'events': events, 'recent_notice' : recent_notice, 'Banners' : Banners})
    # 오늘 날짜 방문자 누적
    # if request.COOKIES.get("is_visit") is None:
    #     tomorrow_date = now + datetime.timedelta(days=1)
    #     tommorow_midnight_str = tomorrow_date.strftime('%Y-%m-%d') + ' 00:00:00'
    #     tommorow_midnight_time = datetime.datetime.strptime(tommorow_midnight_str, '%Y-%m-%d %H:%M:%S')
    #     diff_dt = (tommorow_midnight_time - now).seconds
    #     response.set_cookie('is_visit', 'visited', diff_dt)
    #     today_date = now.strftime('%Y-%m-%d')
    #     vc = VisitorCount.objects.get(visit_date=today_date)
    #     vc.visit_count += 1
    #     vc.save()
    
    # 오늘 날짜 방문자 추출
    # today_visit_count = vc.visit_count
    
    # 모든 날짜 방문자수 총합
    # sum_dict = VisitorCount.objects.aggregate(Sum('visit_count'))
    # total_visit_count = sum_dict['visit_count__sum']
    return render(request, "index.html", {'events': events, 'recent_notice' : recent_notice, 'Banners' : Banners})

def about(request):
    return render(request, "about.html")

def busTime(request):
    return render(request, "busTime.html")

def todayShop(request):
    return render(request, "todayShop.html")

def ads(request):
    return HttpResponse("google.com, pub-4025543581253002, DIRECT, f08c47fec0942fa0")

def totalSearch(request):
    if request.method == 'POST':
        # 검색어 저장
        searched = request.POST['searched']
        # 모드별 검색
        if request.POST['search_mode'] == 'shop' and searched:
            shop_qs1 = list(Cafe.objects.filter(name__contains=searched))
            shop_qs2 = list(Bar.objects.filter(name__contains=searched))
            shop_qs3 = list(Restaurant.objects.filter(name__contains=searched))
            shop_list = shop_qs1 + shop_qs2 + shop_qs3
            return render(request, 'shopList.html', {'shop_list': shop_list, 'searched': searched})
        elif request.POST['search_mode'] == 'menu' and searched:
            menu_qs1 = list(CafeMenu.objects.filter(name__contains=searched))
            menu_qs2 = list(BarMenu.objects.filter(name__contains=searched))
            menu_qs3 = list(RestaurantMenu.objects.filter(name__contains=searched))
            menu = menu_qs1 + menu_qs2 + menu_qs3
            menus = sorted(menu, key=lambda x: x.price, reverse=False)
            return render(request, 'searchResult.html', {'menus': menus, 'searched': searched})
        else:
            return render(request, 'search.html')
    else:
        return render(request, 'search.html')