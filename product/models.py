from django.conf import settings
from django.db import models
from datetime import datetime

class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='products/')
    minBidPrice = models.IntegerField()
    details = models.TextField()
    end_date = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.title

    def is_end_date(self):
        return datetime.now()>self.end_date