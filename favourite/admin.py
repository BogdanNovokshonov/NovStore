from django.contrib import admin
from .models import favItem, fav
# Register your models here.

class favAdmin(admin.ModelAdmin):
    list_display = ('fav_id', 'date_added')

class favItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'fav', 'quantity', 'is_active')

admin.site.register(fav, favAdmin)
admin.site.register(favItem, favItemAdmin)