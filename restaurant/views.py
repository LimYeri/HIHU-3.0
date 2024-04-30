from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from django.db.models import Q
from restaurant.models import Restaurant, RestaurantMenu

import random

class restaurantList(ListView):
    model = Restaurant
    ordering = 'name' # 식당 이름 기준 내림차순 정렬
    context_object_name = 'shop_list'
    template_name = 'shopList.html'
    paginate_by = 6
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            # 검색어 저장
            searched = request.POST['searched']
            # 모드별 검색
            if request.POST['search_mode'] == 'shop' and searched:
                shop_list = Restaurant.objects.filter(name__contains=searched)
                return render(request, 'shopList.html', {'shop_list': shop_list, 'searched': searched})
            elif request.POST['search_mode'] == 'menu' and searched:
                menus = RestaurantMenu.objects.filter(name__contains=searched).order_by('price')
                return render(request, 'searchResult.html', {'menus': menus, 'searched': searched})
            else:
                return redirect('restaurantList')
        else:
            return redirect('restaurantList')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shopKind'] = "식당"
        return context


class restaurantDetail(DetailView):
    model = Restaurant
    ordering = 'name'
    context_object_name = 'shopDetail'
    template_name = 'shopDetail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shopKind'] = "식당"
        context['shopList'] = Restaurant.objects.all().order_by('name')
        
        shop_menu = {}
        # 해당 식당 메뉴의 type을 중복없이 오름차순으로
        for t in RestaurantMenu.objects.filter(shop=self.object.id).values('type').distinct():
            shop_menu[t['type']] = RestaurantMenu.objects.filter(Q(shop=self.object.id) & Q(type=t['type']))
        context['shopMenu'] = shop_menu
        return context


# 오늘 뭐먹지? - 식당
def todayRestaurant(request):
    restaurant_list = Restaurant.objects.all()
    # 랜덤 선택
    today_restaurant = random.choice(restaurant_list)
    return render(request, 'todayShopGet.html', {'shopDetail': today_restaurant, 'shopKind': '식당'})