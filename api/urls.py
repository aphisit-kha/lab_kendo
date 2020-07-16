from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    # api list
    path('accmst_list/', views.AccMstListView.as_view(), name='accmst_list'),
    path('province_list/', views.SetProvListView.as_view(), name='province_list'),
    # session
    path('amphoe_temp/', views.AmphoeTemp, name='amphoe_temp'),
    path('amphoe_clear/', views.AmphoeClear, name='amphoe_clear'),
]