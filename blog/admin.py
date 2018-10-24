from django.contrib import admin
from .models import Article, Categories


admin.site.register(Categories)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'pub_date',
                    'status')
    list_filter = ('status', 'created_at', 'pub_date', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'pub_date'
    ordering = ('status', 'pub_date')
