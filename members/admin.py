from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'last_name', 'first_name', 'email')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)