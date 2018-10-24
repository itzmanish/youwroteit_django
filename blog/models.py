from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone


class Article(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'),
                      ('published', 'Published'),)
    title = models.CharField(max_length=666)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    images = models.ImageField(upload_to='images/')
    category = models.ForeignKey(
        'Categories', null=True, related_name='article_category', on_delete=models.SET_NULL, blank=True)
    author = models.ForeignKey(
        User, null=True, related_name='article_author', on_delete=models.SET_NULL, blank=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    pub_date = models.DateField(default=timezone.now)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='article_author_modifiers', null=True, blank=True)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:50] + "..."

    def pretty_date(self):
        return self.pub_date.strftime('%b %m %Y')

    def get_cat_list(self):  # for now ignore this instance method,
        k = self.category
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent

        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]

    def save(self, *args, **kwargs):
        # Newly created object, so set slug
        self.slug = slugify(self.title)
        super(Article, self,).save(*args, **kwargs)


class Categories(models.Model):
    category_name = models.CharField(max_length=100)
    category_slug = models.SlugField()
    parent = models.ForeignKey(
        'self', blank=True, null=True, on_delete=models.SET_NULL, related_name='children')

    def __str__(self):
        # post.  use __unicode__ in place of
        full_path = [self.category_name]
        # __str__ if you are using python 2
        k = self.parent

        while k is not None:
            full_path.append(k.category_name)
            k = k.parent

        return ' -> '.join(full_path[::-1])

    def save(self, *args, **kwargs):
        self.category_slug = slugify(self.category_name)
        super(Categories, self).save(*args, **kwargs)
