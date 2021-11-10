from django.contrib import admin
from blog.models import MyPost, Comment
# Register your models here.

admin.site.register(MyPost)
admin.site.register(Comment)
