from django.shortcuts import render, get_object_or_404

from .models import Post


def post_list(request):
    """Выводит список всех постов"""
    posts = Post.published.all()
    context = {
        "posts": posts,
    }
    return render(request, "blog/post_list.html", context)


def post_detail(request, year, month, day, post):
    """Выводит конкретный пост"""
    post = get_object_or_404(
        Post,
        slug=post,
        status="published",
        published_date__year=year,
        published_date__month=month,
        published_date__day=day,
    )
    context = {
        "post": post,
    }
    return render(request, "blog/post_detail.html", context)
