from django.shortcuts import render
from projects.models import Project
from api.models import post_create,blog_category

def home(request):
    all_blog = post_create.objects.all().order_by('-id')
    three_blog = post_create.objects.all().order_by('-id')[:3]
    cat = blog_category.objects.all()
    return render(request, 'index.html',{"blogs":all_blog,'tblog':three_blog,'cat':cat})




def contact(request):
    cat = blog_category.objects.all()
    all_blog = post_create.objects.all().order_by('-id')
    return render(request, 'contact.html',{"blogs":all_blog,'cat':cat})

def about(request):
    cat = blog_category.objects.all()
    all_blog = post_create.objects.all().order_by('-id')
    return render(request, 'about.html' ,{"blogs":all_blog,'cat':cat})

def privacy_policy(request):
    cat = blog_category.objects.all()
    all_blog = post_create.objects.all().order_by('-id')
    return render(request, 'privacy-policy.html',{"blogs":all_blog,'cat':cat})

