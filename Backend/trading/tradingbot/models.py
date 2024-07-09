from django.db import models
from django.utils import timezone
import os
from trading import settings

class MarketNews(models.Model):
    CATEGORY_CHOICES = (
        ('general', 'General'),
        ('forex', 'Forex'),
        ('crypto', 'Crypto'),
        ('merger', 'Merger'),
    )

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    datetime = models.IntegerField()
    headline = models.CharField(max_length=255)
    news_id = models.AutoField(primary_key=True)
    image = models.URLField()
    related = models.CharField(max_length=255, blank=True)
    source = models.CharField(max_length=100)
    summary = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.headline
class StockRecommendation(models.Model):
    id = models.AutoField(primary_key=True)
    stock = models.CharField(max_length=100)
    confidence = models.IntegerField()
    advice = models.CharField(max_length=50)
    datetime = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.stock
class Cache(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cache object {self.id} updated at {self.updated_at}"
    
class CSVFile(models.Model):
    file_name = models.CharField(max_length=255)
    file_path = models.FilePathField(path=os.path.join(settings.MEDIA_ROOT, 'csv_files'))

    def __str__(self):
        return self.file_name
    
class TradeSignal(models.Model):
    SIGNAL_CHOICES = [
        ('buy', 'Buy'),
        ('sell', 'Sell'),
    ]

    price = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)
    signal = models.CharField(max_length=4, choices=SIGNAL_CHOICES)

    def __str__(self):
        return f"{self.signal} at {self.price} on {self.time}"
    
class Trade(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    symbol = models.CharField(max_length=10)  # APP 
    action =models.CharField(max_length=10)
    currentPrice = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    entryPrice = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.symbol} - {self.timestamp}"
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    website_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    link = models.URLField(max_length=2000)
    formatted_date = models.DateTimeField()
    article_text = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.website_name}"