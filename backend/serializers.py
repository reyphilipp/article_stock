from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from backend.models import Article, ArticleStock, Stock


class ArticleStockSerializer(ModelSerializer):
    class Meta:
        model = ArticleStock
        fields = ('quantity', 'store_date', 'creator', 'article', 'stock')


class StockSerializer(ModelSerializer):
    class Meta:
        model = Stock
        fields = ('name', 'street', 'zip', 'city', 'creator')

class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'serialnumber', 'description', 'creator')

