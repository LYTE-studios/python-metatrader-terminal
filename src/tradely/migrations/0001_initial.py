# Generated by Django 4.2.7 on 2025-02-03 23:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Terminal",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "platform_type",
                    models.CharField(
                        choices=[("MT4", "MetaTrader 4"), ("MT5", "MetaTrader 5")],
                        max_length=3,
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
                ("host", models.CharField(max_length=255)),
                ("port", models.IntegerField()),
                (
                    "status",
                    models.CharField(
                        choices=[("ON", "Online"), ("OFF", "Offline"), ("BSY", "Busy")],
                        default="OFF",
                        max_length=3,
                    ),
                ),
                ("last_ping", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="TradingAccount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "platform_type",
                    models.CharField(
                        choices=[("MT4", "MetaTrader 4"), ("MT5", "MetaTrader 5")],
                        max_length=3,
                    ),
                ),
                ("account_number", models.CharField(max_length=50)),
                ("password", models.CharField(max_length=255)),
                ("server", models.CharField(max_length=255)),
                (
                    "balance",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=15),
                ),
                (
                    "equity",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=15),
                ),
                ("leverage", models.IntegerField(default=100)),
                ("is_active", models.BooleanField(default=True)),
                ("is_enabled", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Trade",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order_id", models.CharField(max_length=50, unique=True)),
                ("symbol", models.CharField(max_length=10)),
                ("volume", models.DecimalField(decimal_places=2, max_digits=10)),
                ("price_open", models.DecimalField(decimal_places=5, max_digits=15)),
                (
                    "price_close",
                    models.DecimalField(
                        blank=True, decimal_places=5, max_digits=15, null=True
                    ),
                ),
                (
                    "stop_loss",
                    models.DecimalField(
                        blank=True, decimal_places=5, max_digits=15, null=True
                    ),
                ),
                (
                    "take_profit",
                    models.DecimalField(
                        blank=True, decimal_places=5, max_digits=15, null=True
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("BUY", "Buy"), ("SELL", "Sell")], max_length=4
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("OPEN", "Open"),
                            ("CLOSED", "Closed"),
                            ("PENDING", "Pending"),
                            ("CANCELLED", "Cancelled"),
                        ],
                        default="PENDING",
                        max_length=10,
                    ),
                ),
                (
                    "profit",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=15, null=True
                    ),
                ),
                ("opened_at", models.DateTimeField(auto_now_add=True)),
                ("closed_at", models.DateTimeField(blank=True, null=True)),
                (
                    "terminal",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="tradely.terminal",
                    ),
                ),
                (
                    "trading_account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tradely.tradingaccount",
                    ),
                ),
            ],
        ),
    ]
