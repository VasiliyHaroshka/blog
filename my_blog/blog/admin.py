from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "published_date", "status")
    list_filter = ("author", "created_date", "published_date", "status")
    search_fields = ("title", "text")
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ("author",)
    date_hierarchy = "published_date"
    ordering = ("status", "published_date")