from rest_framework import serializers
from .models import MarketNews, StockRecommendation, Cache,TradeSignal,Trade,Article

class MarketNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketNews
        fields = ('category', 'datetime', 'headline', 'image', 'related', 'source', 'summary', 'url')
class StockRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockRecommendation
        fields = ('id', 'stock', 'confidence', 'advice', 'datetime')
class CacheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cache
        fields = ('id', 'value', 'updated_at')

class TradeSignalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeSignal
        fields = ['price', 'time', 'signal']

class TradeingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = ('id', 'timestamp', 'symbol', 'action','currentPrice','entryPrice')
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'website_name', 'title', 'link', 'formatted_date', 'article_text']