from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3


class PostDetail(DetailView):
    queryset = Post.published.all()
    slug_field = "slug"

