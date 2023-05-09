from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Post
from .forms import EmailPostForm


class PostListView(ListView):
    """Отображает список всех постов"""
    queryset = Post.published.all()
    context_object_name = "posts"
    paginate_by = 3


class PostDetail(DetailView):
    """Отображает выбранный пост"""
    queryset = Post.published.all()
    slug_field = "slug"


def post_share(request, post):
    """Обрабатывает форму отправки на email"""
    post = get_object_or_404(Post, slug=post, status="published")
    sent = False
    if request.method == "POST":
        form = EmailPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{data['name']} ({data['email']}) recommend you reading: {post.title}"
            message = f"Read {post.title} at {post_url}\n{data['name']}'s comments: {data['comment']}"
            send_mail(subject, message, "horvasiliy@mail.ru", [data['to']])
            sent = True
    else:
        form = EmailPostForm()
    context = {
        "post": post,
        "form": form,
        "sent": sent,
    }
    return render(request, "blog/share.html", context)
