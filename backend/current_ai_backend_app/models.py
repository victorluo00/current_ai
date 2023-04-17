from django.db import models

class NewsArticle(models.Model):
    source_id = models.CharField(max_length=255, null=True)
    source_name = models.CharField(max_length=255, null=True)
    author = models.CharField(max_length=255, null=True)
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    url = models.URLField(max_length=255, null=True)
    urlToImage = models.URLField(max_length=255, null=True)
    publishedAt = models.DateTimeField(null=True)
    content = models.TextField(null=True)
    summary = models.TextField(null=True)
    tags = models.TextField(null=True)
