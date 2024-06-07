from django.db import models
from django.contrib.auth.models import User
from main.models import Category

# Create your models here.


class Tag(models.Model):
    tag = models.CharField(max_length=255)

    def __str__(self):
        return self.tag


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField()
    image = models.ImageField(upload_to='posts')
    content = models.TextField()
    tag = models.ManyToManyField(Tag)
    created_at = models.DateField()
    author_image = models.ImageField(upload_to='author image')
    author_name = models.CharField(max_length=255)
    author_comment = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='comments', null=True)
    email = models.EmailField()
    website = models.URLField(null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name