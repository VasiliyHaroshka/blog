from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-published_date",)
