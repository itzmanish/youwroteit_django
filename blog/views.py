import json
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView

from blog.api.serializers import ArticleSerializer
from .models import Article


# class ArticleView(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response({'articles': serializer.data})

#     def post(self, request):
#         article = request.data.get('article')

#         # create an article from the aboove data
#         serializer = ArticleSerializer(data=article)
#         if serializer.is_valid(raise_exception=True):
#             article_saved = serializer.save()
#         return Response({'success': 'Article {} created successfully'.format(article_saved.title)})


class ArticleView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
