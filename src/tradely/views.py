from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import TradingAccount, Trade
from .serializers import TradingAccountSerializer, TradeSerializer
from .mt_client import MT5Client


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
            return Response({
                "status": "success",
                "count": len(serializer.data),
                "trades": serializer.data
            })
        except TradingAccount.DoesNotExist:
            return Response({"error": "Account not found"}, status=status.HTTP_404_NOT_FOUND)


class TradeSyncView(APIView):
    """
    Sync trades from MetaTrader terminal
    """
    @staticmethod
    def post(request):
        account_id = request.data.get('account_id')
        if not account_id:
            return Response({"error": "account_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        # user = request.user
        try:
            trading_account = TradingAccount.objects.get(id=account_id)
        except TradingAccount.DoesNotExist:
            return Response({"error": "Trading account not found"}, status=status.HTTP_404_NOT_FOUND)

        connect_status = MT5Client.connect(trading_account.account_number, trading_account.password, trading_account.server)

        if connect_status:
            orders = MT5Client.get_orders()
            MT5Client.shutdown()
            return Response({"status": "success", "orders": orders})
        else:
            MT5Client.shutdown()
            return Response({"error": "Failed to connect to MetaTrader"}, status=status.HTTP_400_BAD_REQUEST)
