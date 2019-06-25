from rest_framework import routers
from django.urls import path, include

from backend.views import ArticleListView, ArticleStockListView, StockListView

router = routers.DefaultRouter()

router.register('article', ArticleListView, base_name='article')
router.register('articleStock', ArticleStockListView, base_name='articleStock')
router.register('stock', StockListView, base_name='stock')

urlpatterns = [
    path('', include(router.urls))
]