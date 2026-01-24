from django.conf import settings
from django.db import models


class LostFoundItem(models.Model):
    STATUS_CHOICES = [
        ('lost', 'Lost'),
        ('found', 'Found'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    location = models.CharField(max_length=200)
    image_url = models.URLField(blank=True)
    contact_info = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='lostfound_items')

    class Meta:
        db_table = 'core_lostfounditem'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.status})"


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('electronics', 'Electronics'),
        ('books', 'Books'),
        ('furniture', 'Furniture'),
        ('others', 'Others'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image_url = models.URLField(blank=True)
    contact_info = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')

    class Meta:
        db_table = 'core_product'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=200)
    preview_text = models.CharField(max_length=300)
    content = models.TextField()
    image_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='news_items')

    class Meta:
        db_table = 'core_news'
        ordering = ['-created_at']

    def __str__(self):
        return self.title