from django.contrib import admin
from blogs.models import Blog, Category, Profile, Comment

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)
