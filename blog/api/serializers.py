from rest_framework import serializers
from blog.models import Article
from datetime import datetime


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    updated_by = serializers.ReadOnlyField(source='updated_by.username')
    category = serializers.ReadOnlyField(source='category.category_name')

    class Meta:
        model = Article
        fields = ('id', 'title', 'slug', 'content', 'image', 'category', 'author',
                  'status', 'created_at', 'pub_date', 'updated_at', 'updated_by')
        # Important trick this will give me url like url/slug instead of url/id
        # https://stackoverflow.com/questions/32201257/django-rest-framework-access-item-detail-by-slug-instead-of-id
        lookup_field = 'slug'

    # title = serializers.CharField()
    # slug = serializers.SlugField()
    # content = serializers.CharField()
    # created_at = serializers.DateTimeField()
