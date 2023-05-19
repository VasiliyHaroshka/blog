from django import template
from django.db.models import Count

from ..models import Post

register = template.Library()


@register.simple_tag(name="count_tags")
def total_posts():
    """Тег для вывода общего количества опубликованных постов"""
    return Post.published.count()


@register.simple_tag()
def most_commented_posts(count=2):
    """Тег для вывода самых комментируемых поста"""
    return Post.published.annotate(total_comments=Count("comments")).order_by("-total_comments")[:count]


@register.inclusion_tag("blog/latest_posts.html")
def display_the_latest_posts(count=3):
    """Тег для вывода 3 последних опубликованных постов"""
    latest_posts = Post.published.all().order_by("-published_date")[:count]
    return {"latest_posts": latest_posts}
