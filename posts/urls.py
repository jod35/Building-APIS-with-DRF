from django.urls import path

from . import views

urlpatterns = [
    path("homepage/", views.homepage, name="posts_home"),
    path("", views.PostListCreateView.as_view(), name="list_posts"),
    path(
        "<int:pk>/",
        views.PostRetrieveUpdateDeleteView.as_view(),
        name="post_detail",
    ),
    path("current_user/", views.get_posts_for_current_user, name="current_user"),
    path(
        "posts_for/",
        views.ListPostsForAuthor.as_view(),
        name="posts_for_current_user",
    ),
]


# djaneiro
