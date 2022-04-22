from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=80)
    reason = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return "Message from " + self.name

class Categorie(models.Model):
    sno = models.AutoField(primary_key = True)
    slug = models.CharField(max_length=100)
    category_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    qoute = models.CharField(max_length=300, default="")
    image = models.ImageField(upload_to = "blog/images", default="")
    created_on = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return self.category_name

class Post(models.Model):
    sno = models.AutoField(primary_key = True)
    slug = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    post_category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = "blog/images", default="")
    created_on = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='+')
    timestamp = models.DateTimeField(auto_now_add=True)