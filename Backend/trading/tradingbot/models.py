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

    def __str__(self):
        return self.headline

class Cache(models.Model):
    id = models.AutoField(primary_key=True)    
    value = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    def is_expired(self):
        if self.expires_at:
            return timezone.now() > self.expires_at
        return False

    def __str__(self):
        return self
    
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