from django.conf import settings
from django.db import models
from datetime import datetime
from django.utils import timezone

from django.db.models.deletion import CASCADE
from account.models import Account

class Product(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='products/')
    minBidPrice = models.IntegerField()
    details = models.TextField()
    end_date = models.DateTimeField(auto_now_add=False,null=False,blank=False)

    def __str__(self):
        return self.title

    def is_end_date(self):
        return timezone.now()>self.end_date

    def total(self):
        return self.objects.count()
    


class Bid(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    bidAmount=models.IntegerField()
    created_at=models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-bidAmount',)
    
    def __str__(self):
        return str(self.product)


