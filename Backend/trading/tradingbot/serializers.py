from rest_framework import serializers
from .models import MarketNews, StockRecommendation, Cache,TradeSignal

class MarketNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketNews
        fields = ('category', 'datetime', 'headline', 'image', 'related', 'source', 'summary', 'url')
class StockRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockRecommendation
        fields = ('stock', 'confidence', 'advice')
class CacheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cache
        fields = ('id', 'value', 'created_at', 'updated_at', 'expires_at')

class TradeSignalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeSignal
        fields = ['price', 'time', 'signal']