from django.urls import path
from . import views

urlpatterns = [
    path("news/", views.MarketNewsView.as_view()),
    path("llm/",views.ProcessNewsView.as_view() ),
    path("cash/",views.CacheView.as_view()),
    path("cash/<int:pk>/", views.CacheView.as_view()),  # GET by ID UPDATE by ID
]