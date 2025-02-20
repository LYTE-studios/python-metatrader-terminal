from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = "tradely"

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/mt-account/", views.MTAccountAuthView.as_view(), name="mt-auth"),
    path("trades/<int:account_id>/", views.TradeListView.as_view(), name="trade-list"),
    path("mt5/get_trades/", views.TradeSyncView.as_view(), name="trade-sync"),
    path("mt5/get_history/", views.TradeHistoryView.as_view(), name="trade-history"),
    path("mt5/connect/", views.MT5ConnectView.as_view(), name="mt5-connect"),
]
