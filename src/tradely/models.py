from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


class TradingAccount(models.Model):
    MT4 = "MT4"
    MT5 = "MT5"
    PLATFORM_CHOICES = [
        (MT4, "MetaTrader 4"),
        (MT5, "MetaTrader 5"),
    ]

    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="trading_accounts"
    )
    platform_type = models.CharField(max_length=3, choices=PLATFORM_CHOICES)
    account_number = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    server = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    equity = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    leverage = models.IntegerField(default=100)
    is_active = models.BooleanField(default=True)
    is_enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s {self.get_platform_type_display()} Account"


class Terminal(models.Model):
    ONLINE = "ON"
    OFFLINE = "OFF"
    BUSY = "BSY"
    STATUS_CHOICES = [
        (ONLINE, "Online"),
        (OFFLINE, "Offline"),
        (BUSY, "Busy"),
    ]

    platform_type = models.CharField(
        max_length=3, choices=TradingAccount.PLATFORM_CHOICES
    )
    name = models.CharField(max_length=100, unique=True)
    host = models.CharField(max_length=255)
    port = models.IntegerField()
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default=OFFLINE)
    last_ping = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.get_platform_type_display()})"


class Trade(models.Model):
    BUY = "BUY"
    SELL = "SELL"
    TYPE_CHOICES = [
        (BUY, "Buy"),
        (SELL, "Sell"),
    ]

    OPEN = "OPEN"
    CLOSED = "CLOSED"
    PENDING = "PENDING"
    CANCELLED = "CANCELLED"
    STATUS_CHOICES = [
        (OPEN, "Open"),
        (CLOSED, "Closed"),
        (PENDING, "Pending"),
        (CANCELLED, "Cancelled"),
    ]

    trading_account = models.ForeignKey(TradingAccount, on_delete=models.CASCADE)
    terminal = models.ForeignKey(
        Terminal, on_delete=models.SET_NULL, null=True, blank=True
    )
    order_id = models.CharField(max_length=50, unique=True)  # MetaTrader's ticket ID
    symbol = models.CharField(max_length=10)  # e.g., EURUSD
    volume = models.DecimalField(max_digits=10, decimal_places=2)  # Lot size
    price_open = models.DecimalField(max_digits=15, decimal_places=5)
    price_close = models.DecimalField(
        max_digits=15, decimal_places=5, null=True, blank=True
    )
    stop_loss = models.DecimalField(
        max_digits=15, decimal_places=5, null=True, blank=True
    )
    take_profit = models.DecimalField(
        max_digits=15, decimal_places=5, null=True, blank=True
    )
    type = models.CharField(max_length=4, choices=TYPE_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    profit = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    opened_at = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Trade #{self.order_id} ({self.symbol} {self.type})"
