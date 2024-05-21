from rest_framework.response import Response
from rest_framework.views import APIView
from controllers.tradingStrategyController import run_strategy

class TradingStrategyAPIView(APIView):
    def get(self, request):

        actions = run_strategy()
        return Response(actions)