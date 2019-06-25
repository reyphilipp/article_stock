from django.contrib.auth.models import User
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=120)
    serialnumber = models.IntegerField(unique=True)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class ArticleStock(models.Model):
    quantity = models.IntegerField()
    store_date = models.DateTimeField()
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    article = models.ForeignKey('Article', related_name='Articles', on_delete=models.DO_NOTHING)
    stock = models.ForeignKey('Stock', related_name='Stocks', on_delete=models.DO_NOTHING)


class Stock(models.Model):
    name = models.CharField(max_length=120)
    street = models.CharField(max_length=120)
    zip = models.CharField(max_length=10)
    city = models.CharField(max_length=120)
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
