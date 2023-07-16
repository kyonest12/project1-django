from django.contrib import admin
from blogs.models import Blog, Category, Profile, Comment

class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'date', 'user')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)

