from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Article(models.Model):
    STATUS = (('Published', 'published'),
              ('Draft', 'draft'))
    title = models.CharField(max_length=500)
    slug = models.SlugField(unique=True, max_length=500)
    content = RichTextUploadingField()
    image = models.ImageField(upload_to='images')
    category = models.TextField()
    author = models.ForeignKey(
        User, null=True, related_name='article_author', on_delete=models.SET_NULL, blank=True)
    pub_date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='article_author_modifiers', null=True, blank=True)
    status = models.CharField(choices=STATUS, default='Draft', max_length=20)

    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title

    def get_cat_list(self):  # for now ignore this instance method,
        k = self.category
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent

        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        # Newly created object, so set slug
        self.slug = slugify(self.title)
        super(Article, self,).save(*args, **kwargs)


# class Categories(models.Model):
#     category_name = models.CharField(max_length=100)
#     category_slug = models.SlugField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     parent = models.ForeignKey(
#         'self', blank=True, null=True, on_delete=models.SET_NULL, related_name='children')

#     def __str__(self):
#         # post.  use __unicode__ in place of
#         full_path = [self.category_name]
#         # __str__ if you are using python 2
#         k = self.parent

#         while k is not None:
#             full_path.append(k.category_name)
#             k = k.parent

#         return ' -> '.join(full_path[::-1])

#     def save(self, *args, **kwargs):
#         self.category_slug = slugify(self.category_name)
#         super(Categories, self).save(*args, **kwargs)


# class Subscribe(models.Model):
#     email_id = models.EmailField(null=True, blank=True)
#     timestamp = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return self.email_id


# class Comment(models.Model):
#     post = models.ForeignKey(
#         'Article', on_delete=models.CASCADE, related_name='comments')
#     name = models.CharField(max_length=80)
#     email = models.EmailField()
#     body = models.TextField()
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     active = models.BooleanField(default=True)

#     class Meta:
#         ordering = ('created',)

#     def __str__(self):
#         return 'Comment by {} on {}'.format(self.name, self.post)
