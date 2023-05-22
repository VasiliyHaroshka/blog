from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords

from .models import Post


class LatestPostFeed(Feed):
    title = "My blog"
    link = "/blog/"
    description = "New posts of the blog"

    def items(self):
        """Формирование объектов включенных в рассылку RSS"""
        return Post.published.all()[:3]

    def item_title(self, item):
        """Формирование заголовка поста RSS"""
        return item.title

    def item_description(self, item):
        """Формирование содержимого поста RSS"""
        return truncatewords(item.text, 30)
