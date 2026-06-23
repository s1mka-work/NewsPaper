from django.contrib.auth.models import User
from django.db import models

from .censor import censor, BAD_WORDS


class Author(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.FloatField(default=0)

    def update_rating(self):
        posts = Post.objects.filter(author_id=self).values('rating')
        comments = Comment.objects.filter(user_id=self.user_id).values('rating')
        posts_comments = Comment.objects.filter(post_id__author_id=self).values('rating')
        posts_rate = 0
        comments_rate = 0
        posts_comments_rate = 0

        for p in posts:
            posts_rate += p['rating'] * 3

        for c in comments:
            comments_rate += c['rating']

        for pc in posts_comments:
            posts_comments_rate += pc['rating']

        self.rating = posts_rate + comments_rate + posts_comments_rate
        self.save()

class Category(models.Model):
    name = models.CharField(unique=True, max_length=50)

class Post(models.Model):
    news = 'N'
    article = 'A'
    CATEGORY_CHOICES = [
        (news, 'Новость'),
        (article, 'Статья')]

    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, through='PostCategory')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=1)
    date = models.DateTimeField(auto_now_add=True)
    header = models.TextField()
    text = models.TextField()
    rating = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        self.header = censor(self.header, BAD_WORDS)
        self.text = censor(self.text, BAD_WORDS)

        super().save(*args, **kwargs)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:125] + '...'

    def __str__(self):
        return f'{self.header} \n {self.text[:50]}...'


class PostCategory(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
