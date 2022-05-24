from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("posts/", include("posts.urls")),
    path("auth/", include("accounts.urls")),
]
