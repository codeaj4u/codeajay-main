from django.shortcuts import render
from api.models import post_create,blog_category


def singleblog(request,slug):
    top_blog = post_create.objects.get(slug=slug)
    all_blog = post_create.objects.all().order_by('-id')
    cat = blog_category.objects.all()

    return render(request, "post.html", {"blogs": all_blog,"topblog":top_blog,'cat':cat})


def category(request,cat):
    filtered_posts = post_create.objects.filter(category__slug=cat).order_by('-id')
    cat = blog_category.objects.all()
    all_blog = post_create.objects.all().order_by('-id')
    return render(request, 'category.html',{'tblog': filtered_posts,'cat':cat,"blogs": all_blog})