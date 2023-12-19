from django.contrib.sitemaps import Sitemap
from .models import post_create

class blog_post_sitemap(Sitemap):

    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return post_create.objects.all()

    def lastmod(self, obj):
        return obj.updated_at



class custom_sitemap(Sitemap):

    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return ['','/about','/contact']

    def location(self, item):
        return item

