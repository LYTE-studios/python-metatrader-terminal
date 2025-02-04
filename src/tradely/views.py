from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import TradingAccount, Trade
from .serializers import TradingAccountSerializer, TradeSerializer

class MTAccountAuthView(generics.CreateAPIView):
    queryset = TradingAccount.objects.all()
    serializer_class = TradingAccountSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TradeListView(APIView):
    """
    Fetch trades for authenticated account
    """
    def get(self, request, account_id):
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