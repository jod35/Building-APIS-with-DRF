from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=50)

    class Meta:
        model = Post
        fields = ["id", "title", "content", "created"]
