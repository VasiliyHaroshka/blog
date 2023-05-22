from django.contrib.sitemaps import Sitemap

from .models import Post


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        """Возвращает Queryset объектов, которые будут отображаться на карте сайта"""
        return Post.published.all()

    def lastmod(self, obj):
        """Возвращает время последней модификации объектов Queryset(а) из метода items"""
        return obj.updated_date
