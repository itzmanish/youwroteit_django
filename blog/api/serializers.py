from rest_framework import serializers
from blog.models import Article
from datetime import datetime


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'slug', 'content', 'created_at')

    # title = serializers.CharField()
    # slug = serializers.SlugField()
    # content = serializers.CharField()
    # created_at = serializers.DateTimeField()
