from . import views
from django.urls import path

urlpatterns = [
    path("homepage/", views.homepage, name="posts_home"),
    path("", views.list_posts, name="list_posts"),
    path("<int:post_id>", views.post_detail, name="post_detail"),
    path("update/<int:post_id>/", views.update_post, name="update_post"),
    path("delete/<int:post_id>/", views.delete_post, name="delete_post"),
]


# djaneiro
