from django.contrib import admin

from restaurant.models import *

class restaurantMenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', 'price', 'shop']
    list_display_links = ['id']
    list_filter = ['type', 'shop']
    list_editable = ['name', 'type', 'price', 'shop']

class restaurant_Admin(admin.ModelAdmin):
    list_display = ['name', 'shopType', 'time', 'phone']
    list_display_links = ['name']
    list_editable = ['shopType', 'time', 'phone']

admin.site.register(Restaurant, restaurant_Admin)
admin.site.register(RestaurantMenu, restaurantMenuAdmin)