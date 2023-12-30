from django.contrib import admin
from .models import post_create,blog_category,Comments



admin.site.register(post_create)
admin.site.register(blog_category)
admin.site.register(Comments)

