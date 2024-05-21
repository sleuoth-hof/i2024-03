from rest_framework.response import Response
from rest_framework.views import APIView
from  serializer import NewsEvaluationSerializer
from controllers.evaluationController import evaluate_news
from   models.newsEvaluation import NewsEvaluation


class EvaluateNewsAPIView(APIView):
    def get(self, request):
        evaluate_news()
        news_evaluations = NewsEvaluation.objects.all()
        serializer = NewsEvaluationSerializer(news_evaluations, many=True)
        return Response(serializer.data)