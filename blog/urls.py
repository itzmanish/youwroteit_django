from django.urls import path

from .views import ArticleView, ArticleDetailView

app_name = 'blog'

urlpatterns = [
    path('articles/', ArticleView.as_view()),
    # path('subscribe/', views.subscribe, name="subscribe"),
    # path('tag/<slug:tag_slug>/', views.article_home, name='article_by_tag'),
    path('articles/<int:pk>/', ArticleDetailView.as_view()),
]
