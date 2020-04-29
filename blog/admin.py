from django.contrib import admin
from .models import Post
# from .models import Post, BlogComment

# Register your models here.

admin.site.register(Post)
# admin.site.register((Post, BlogComment))