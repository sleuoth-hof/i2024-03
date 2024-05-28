from . import views
from django.urls import path
ws_urlpatterns = [
    path("live/", views.TradeWebSocket.as_asgi())
]