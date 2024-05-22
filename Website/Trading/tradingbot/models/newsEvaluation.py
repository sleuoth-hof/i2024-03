from django.db import models


class NewsEvaluation(models.Model):
    news_date = models.DateField()
    news_name = models.CharField(max_length=500)
    confidence = models.FloatField()
    advice = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.news_date} - {self.news_name}"
