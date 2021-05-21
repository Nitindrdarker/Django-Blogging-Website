from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    def get_absolute_url (self):
        return reverse('home')
class Profile(models.Model):
    #associate this model with our user model
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    profile_pic =  models.ImageField(null=True, blank=True, upload_to='images/profile/', default='images/default/pp.jpg')
    website_url = models.CharField(max_length=255, null=True, blank=True)
    facebook_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    pinterest_url = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return str(self.user)
    def get_absolute_url (self):
        return reverse('home')
class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='uncategorised')
    Snippet = models.CharField(max_length=255)
    likes = models.ManyToManyField(User, related_name='blog_post')#blog and user likes are many to many relaton

    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title + " | " + str(self.author)
    def get_absolute_url (self):
        return reverse('home')
class Comment(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,related_name='comments', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '{} | {}'.format(self.post.title, str(self.user.username))