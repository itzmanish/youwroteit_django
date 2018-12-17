from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Article, Subscribe, Comment
from django.http import HttpResponse, JsonResponse
from .utils import SendSubscribeMail
from .forms import CommentForm
from taggit.models import Tag


def google_login(request):
    return render(request, 'google_auth.html')


def article_home(request, tag_slug=None):
    object_list = Article.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 6)  # 6 posts in each page
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    return render(request, 'blog/article/home.html', {'articles': articles, 'tag': tag})


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug, status='published',)
    # List of active comments for this post
    comments = article.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            # Assign the current post to the comment
            new_comment = comment_form.save(commit=False)
            new_comment.post = article
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'blog/article/article.html', {'article': article, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})


def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email_id']
        email_qs = Subscribe.objects.filter(email_id=email)
        if email_qs.exists():
            data = {"status": "404"}
            return JsonResponse(data)
        else:
            Subscribe.objects.create(email_id=email)
            # Send the Mail, Class available in utils.py
            SendSubscribeMail(email)
    return HttpResponse("/")
