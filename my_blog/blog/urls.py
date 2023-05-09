from django.urls import path

from .views import PostListView, PostDetail, post_share

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("<slug:slug>/", PostDetail.as_view(), name="post_detail"),
    path("<slug:post>/share/", post_share, name="post_share"),
]