from django.shortcuts import render
from api.models import post_create


def singleblog(request,slug):
    top_blog = post_create.objects.get(slug=slug)
    print(top_blog.slug)
    all_blog = post_create.objects.all().order_by('-id')
    return render(request, "post.html", {"blogs": all_blog,"topblog":top_blog})