from django.urls import path

from .views import PostListView, PostDetail

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("<slug:slug>/", PostDetail.as_view(), name="post_detail"),
    # path("<int:year>/<int:month>/<int:day>/<slug:post>/", post_detail, name="post_detail"),
]