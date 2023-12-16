from django.shortcuts import render
from projects.models import Project
from api.models import post_create

def home(request):
    all_blog = post_create.objects.all().order_by('-id')
    three_blog = post_create.objects.all().order_by('-id')[:3]

    return render(request, 'index.html',{"blogs":all_blog,'tblog':three_blog})


