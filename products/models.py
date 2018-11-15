from django.db import models
from django.urls import reverse
from django.utils import timezone

class Product(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=300)
    url = models.URLField(max_length=200)
    upvotes = models.IntegerField(default=1)
    image = models.ImageField(upload_to='media/images/', blank=True)
    icon = models.ImageField(upload_to='media/images/', blank=True)
    body = models.TextField(blank=True)
    hunter = models.CharField(max_length=200, blank=True)
    pub_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.id)])
