from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('main/',views.main, name='main'),
    path('index/',views.index, name='test'),
    path("news/", views.MarketNewsView.as_view()),
    path("llm/",views.ProcessNewsView.as_view() ),
    path("cash/",views.CacheView.as_view()),
    path("cash/<int:pk>/", views.CacheView.as_view()),  # GET by ID UPDATE by ID
    path('stockllm/', views.StockRecommendationView.as_view())
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)