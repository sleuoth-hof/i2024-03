from django.db import models


class News(models.Model):
    category = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    headline = models.CharField(max_length=500)
    image = models.URLField()
    related = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    summary = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.headline
