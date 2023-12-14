from django.urls import path
from . import views

urlpatterns = [
    path('', views.fav, name='favourite'),
    path('add_fav/<int:product_id>/', views.add_fav, name='add_fav'),
    path('remove_fav/<int:product_id>/<int:fav_item_id>/', views.remove_fav, name='remove_fav'),
    path('remove_fav_item/<int:product_id>/<int:fav_item_id>/', views.remove_fav_item, name='remove_fav_item'),
]
