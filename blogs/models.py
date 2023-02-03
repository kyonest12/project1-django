from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class NameField(models.CharField):

    def get_prep_value(self, value):
        return str(value).lower()

class Category(models.Model):
    name = NameField(max_length=500, unique=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home_page')

class Profile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile')
    facebook_url = models.CharField(max_length=500, null=True, blank=True)
    instagram_url = models.CharField(max_length=500, null=True, blank=True)
    twitter_url = models.CharField(max_length=500, null=True, blank=True)
    def __str__(self):
        return str(self.user)
    def get_absolute_url(self):
        return reverse('home_page')

class Blog(models.Model):
    name = models.CharField(max_length=500)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    summary = models.TextField(max_length=300)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    content = RichTextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blogs_posts')

    def __str__(self):
        return self.name

    def total_like(self):
        return self.likes.count()

    def tolal_comment(self):
        return self.comments.count()

    def get_absolute_url(self):
        return reverse('home_page')

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.blog.name) + ("---") + (self.user.username)
