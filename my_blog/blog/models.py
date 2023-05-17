from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="published")


class Post(models.Model):
    """Модель описания поста"""
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    title = models.CharField("Заголовок", max_length=250)
    slug = models.SlugField("Слаг", max_length=100, unique_for_date="published_date")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_post", verbose_name="Автор")
    text = models.TextField("Текст")
    published_date = models.DateField("Дата публикации", default=timezone.now())
    created_date = models.DateField("Дата создания", auto_now_add=True)
    updated_date = models.DateField("Дата обновления", auto_now=True)
    status = models.CharField("Статус", max_length=10, choices=STATUS_CHOICES, default="draft")
    tags = TaggableManager()

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail",
                       args=[
                           self.published_date.year,
                           self.published_date.month,
                           self.published_date.day,
                           self.slug,
                       ])

    class Meta:
        ordering = ("-published_date",)


class Comment(models.Model):
    """Модель комментария"""
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    text = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} leave comment on post: {self.post}."

    class Meta:
        ordering = ("created",)
