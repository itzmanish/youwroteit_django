from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ArticleViewSet, basename='article')
urlpatterns = router.urls

# from django.urls import path

# from .views import (
#     ArticleView,
#     ArticleDetailView,
#     ArticleDeleteView,
#     ArticleCreateView,
#     ArticleUpdateView
# )

# app_name = 'blog'

# urlpatterns = [
#     path('articles/', ArticleView.as_view()),
#     path('articles/create', ArticleCreateView.as_view()),
#     path('articles/<int:pk>/update', ArticleUpdateView.as_view()),
#     path('articles/<int:pk>/delete', ArticleDeleteView.as_view()),
#     # path('subscribe/', views.subscribe, name="subscribe"),
#     # path('tag/<slug:tag_slug>/', views.article_home, name='article_by_tag'),
#     path('articles/<int:pk>/', ArticleDetailView.as_view()),
# ]
