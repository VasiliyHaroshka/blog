from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from .models import Post


def post_list(request):
    """Выводит список всех постов"""
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        "posts": posts,
        "page": page,
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
