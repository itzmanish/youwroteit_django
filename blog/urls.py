from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.article_home, name='article_home'),
    path('subscribe/', views.subscribe, name="subscribe"),
    path('tag/<slug:tag_slug>/', views.article_home, name='article_by_tag'),
    path('<slug:slug>/', views.article_detail, name='article_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
