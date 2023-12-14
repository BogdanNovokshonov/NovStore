from django.contrib import admin
from .models import FavItem, Fav
# Register your models here.

class favAdmin(admin.ModelAdmin):
    list_display = ('fav_id', 'date_added')

class favItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'fav', 'quantity', 'is_active')

admin.site.register(Fav, favAdmin)
admin.site.register(FavItem, favItemAdmin)