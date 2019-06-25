from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from backend.models import Article, ArticleStock, Stock
from backend.serializers import ArticleSerializer, ArticleStockSerializer, StockSerializer


class ArticleListView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleStockListView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = ArticleStock.objects.all()
    serializer_class = ArticleStockSerializer

class StockListView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

