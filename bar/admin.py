from django.contrib import admin
from bar.models import *

class barMenuAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', 'price', 'shop']
    list_display_links = ['id']
    list_filter = ['type', 'shop']
    list_editable = ['name', 'type', 'price', 'shop']

class bar_Admin(admin.ModelAdmin):
    list_display = ['name', 'time', 'phone']
    list_display_links = ['name']
    list_editable = ['time', 'phone']

admin.site.register(Bar, bar_Admin)
admin.site.register(BarMenu, barMenuAdmin)