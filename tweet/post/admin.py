from django.contrib import admin
from .models import Post
from django.contrib.auth.apps import AuthConfig
from django.contrib.auth.models import Group

AuthConfig.verbose_name = "Users Settings"

admin.site.site_header = "Tweet Project Administration"

admin.site.index_title = "Welcome to Tweet Project Admin"

admin.site.unregister(Group)
# Register your models here.
admin.site.register(Post)