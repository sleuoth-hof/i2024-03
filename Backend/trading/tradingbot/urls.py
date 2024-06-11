from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('main/',views.main, name='main'),
    path('admin/',admin.site.urls, name='admin'),
    path('index/',views.index, name='test'),
    path("news/", views.MarketNewsView.as_view()),
    path("llm/",views.ProcessNewsView.as_view() ),
    path("cash/",views.CacheView.as_view()),
    path("cash/<int:pk>/", views.CacheView.as_view()),  # GET by ID UPDATE by ID
    path('stockllm/', views.StockRecommendationView.as_view()),
    path('get_price/<str:ticker>/', views.get_price, name='get_price')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)