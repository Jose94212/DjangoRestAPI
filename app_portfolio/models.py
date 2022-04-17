
from django.db import models

# Create your models here.

class Post(models.Model):
    company_name=models.CharField(max_length=200)
    shares=models.IntegerField()
    avg_price=models.DecimalField(max_digits=50, decimal_places=2, blank=True, null=True)
    buy_date=models.DateField()
    invested_amount=models.DecimalField(max_digits=50, decimal_places=2, blank=True, null=True)
    sell_price=models.DecimalField(max_digits=50, decimal_places=2, blank=True, null=True)
    sell_date=models.DateField()

