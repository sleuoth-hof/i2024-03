from rest_framework import serializers
from models.newsEvaluation import NewsEvaluation

class NewsEvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsEvaluation
        fields = '__all__'