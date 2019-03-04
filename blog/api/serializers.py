from rest_framework import serializers
from blog.models import Article
from datetime import datetime


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'slug', 'content', 'created_at')
        # Important trick this will give me url like url/slug instead of url/id
        lookup_field = 'slug'

    # title = serializers.CharField()
    # slug = serializers.SlugField()
    # content = serializers.CharField()
    # created_at = serializers.DateTimeField()
