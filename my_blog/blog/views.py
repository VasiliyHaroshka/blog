from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect

from taggit.models import Tag

from .models import Post
from .forms import EmailPostForm, CommentForm


def post_list(request, tag_slug=None):
    """Отображает список всех постов"""
    object_list = Post.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        "page": page,
        "posts": posts,
        "tags": tag,
    }
    return render(request, "blog/post_list.html", context)


def post_detail(request, year, month, day, post):
    """Отображает выбранный пост"""
    post = get_object_or_404(Post, slug=post,
                             published_date__year=year, published_date__month=month, published_date__day=day)
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    context = {
        "post": post,
        "comments": comments,
        "new_comment": new_comment,
        "comment_form": comment_form,
    }
    return render(request, "blog/post_detail.html", context)


def post_share(request, post_id):
    """Обрабатывает форму отправки на email"""
    post = get_object_or_404(Post, id=post_id, status="published")
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
