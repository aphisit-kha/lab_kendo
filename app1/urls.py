from django.urls import path
from app1 import views

app_name = 'app1'

urlpatterns = [
    path('province_index/', views.index, name='province_index'),
    path('province_create/', views.create, name='province_create'),
    path('province_refresh/<provcod>', views.refresh, name='province_refresh'),
    path('province_update/<provcod>', views.update, name='province_update'),
]