from django.db import models


class Contacts(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name



class BlogPost(models.Model):
    # id = models.AutoField()
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date = models.DateField()
    text = models.TextField()
    categories = models.ManyToManyField(Category, related_name='blog_posts')

class Comment(models.Model):
    post = models.ForeignKey('BlogPost', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'







