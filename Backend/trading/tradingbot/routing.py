from . import views
from django.urls import path

from django.urls import re_path

from . import consumers

# ws_urlpatterns = [
#     path("live/", views.TradeWebSocket.as_asgi()),
    
# ]

websocket_urlpatterns = [
    re_path(r'ws/stock_prices/$', consumers.StockPriceConsumer.as_asgi()),
]