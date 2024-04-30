from django.contrib import admin
from cafe.models import *

class cafeMenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', 'price', 'shop']
    list_display_links = ['id']
    list_filter = ['type', 'shop']
    list_editable = ['name', 'type', 'price', 'shop']

class cafe_Admin(admin.ModelAdmin):
    list_display = ['name', 'time', 'phone']
    list_display_links = ['name']
    list_editable = ['time', 'phone']

admin.site.register(Cafe, cafe_Admin)
admin.site.register(CafeMenu, cafeMenuAdmin)