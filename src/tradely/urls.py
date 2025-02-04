from django.urls import path
from . import views

app_name = 'tradely'

urlpatterns = [
    path('auth/mt-account/', views.MTAccountAuthView.as_view(), name='mt-auth'),
    path('trades/<int:account_id>/', views.TradeListView.as_view(), name='trade-list'),
]