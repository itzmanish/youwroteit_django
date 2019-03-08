from django.contrib import admin
from .models import Article, Categories


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'author', 'status', 'pub_date',
                    )
    list_select_related = (
        'category',
    )
    list_filter = ('created_at', 'pub_date',)
    search_fields = ('title', 'content', 'author')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('status',)
    date_hierarchy = 'pub_date'
    ordering = ('pub_date',)

    def save_model(self, request, obj, form, change):
        if not obj.author.id:
            obj.author = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('post', 'name', 'created', 'updated', 'active')
#     list_filter = ('active', 'created', 'updated', 'name')
#     search_fields = ('post', 'name')
#     date_hierarchy = 'updated'
#     ordering = ('active', 'updated')


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_slug', 'created_at',)
    list_filter = ('category_name',)
    prepopulated_fields = {'category_slug': ('category_name',)}
    search_fields = ('category_name',)
    date_hierarchy = 'updated_at'
    ordering = ('updated_at',)


# admin.site.register(Subscribe)
