from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import TradingAccount, Trade
from .serializers import TradingAccountSerializer, TradeSerializer
from .mt_client import MT5Client
from django.contrib.auth import get_user_model


class MTAccountAuthView(generics.CreateAPIView):
    queryset = TradingAccount.objects.all()
    serializer_class = TradingAccountSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TradeListView(APIView):
    """
    Fetch trades for authenticated account
    """

    @staticmethod
    def get(request, account_id):
        try:
            account = TradingAccount.objects.get(id=account_id)
            trades = Trade.objects.filter(trading_account=account)
            serializer = TradeSerializer(trades, many=True)

            # Placeholder: Add actual MT trade sync
            return Response(
                {
                    "status": "success",
                    "count": len(serializer.data),
                    "trades": serializer.data,
                }
            )
        except TradingAccount.DoesNotExist:
            return Response(
                {"error": "Account not found"}, status=status.HTTP_404_NOT_FOUND
            )


class MT5ConnectView(APIView):
    """
    Connect to MetaTrader5 and return login status
    """

    @staticmethod
    def post(request):
        account = request.data.get("account")
        password = request.data.get("password")
        server = request.data.get("server")
        if not account or not password or not server:
            return Response(
                {"error": "parameters are required"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            connect_status = MT5Client.connect(
                account,
                password,
                server,
            )

            if connect_status["status"]:
                User = get_user_model()
                user, created = User.objects.get_or_create(
                    username=account,
                    defaults={"email": f"{account}@tradely.io", "password": password},
                )
                account_info = connect_status["account_info"]
                trading_account, created = TradingAccount.objects.update_or_create(
                    account_number=account,
                    user=user,
                    defaults={
                        "balance": account_info.balance,
                        "equity": account_info.equity,
                        "password": password,
                        "server": server,
                    },
                )

                return Response(
                    {"status": "success", "account_info": account_info._asdict()}
                )
            else:
                return Response(
                    {
                        "error": "Failed to connect to MetaTrader",
                        "error_code": connect_status["error_code"],
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class TradeSyncView(APIView):
    """
    Sync trades from MetaTrader terminal
    """

    @staticmethod
    def post(request):
        account_id = request.data.get("account_id")
        if not account_id:
            return Response(
                {"error": "account_id is required"}, status=status.HTTP_400_BAD_REQUEST
            )

        # user = request.user
        try:
            trading_account = TradingAccount.objects.get(account_number=account_id)
        except TradingAccount.DoesNotExist:
            return Response(
                {"error": "Trading account not found"}, status=status.HTTP_404_NOT_FOUND
            )
        try:
            connect_status, account_info = MT5Client.connect(
                trading_account.account_number,
                trading_account.password,
                trading_account.server,
            )

            if connect_status:
                orders = MT5Client.get_orders()
                MT5Client.shutdown()
                return Response({"status": "success", "orders": orders})
            else:
                MT5Client.shutdown()
                return Response(
                    {"error": "Failed to connect to MetaTrader"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
