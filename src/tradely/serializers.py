from rest_framework import serializers
from .models import TradingAccount, Trade


class TradingAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradingAccount
        fields = ['user', 'platform_type', 'account_number', 'password', 'server', 'id']
        read_only_fields = ['id']
        extra_kwargs = {'user': {'required': False}}

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = '__all__'
        read_only_fields = ['opened_at', 'closed_at']
