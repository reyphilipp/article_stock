from django.contrib import admin

from backend.models import Article, Stock, ArticleStock


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    pass

@admin.register(ArticleStock)
class ArticleStockAdmin(admin.ModelAdmin):
    pass
