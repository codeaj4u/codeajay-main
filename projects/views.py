from django.shortcuts import render
from api.models import post_create,blog_category
import asyncio
from account.views import send_telegram_message



def singleblog(request,slug):


    if request.method == "POST":
        name = request.POST['name']
        contact = request.POST['contact']
        email = request.POST['email']
        message = request.POST['message']

        mes = f'''
    codeAjay.in

    Name : {name}
    Contact : {contact}
    Email : {email}
    Message : {message}
    '''

        print(mes)
        asyncio.run(send_telegram_message(mes))
        print("send !!")


    top_blog = post_create.objects.get(slug=slug)
    all_blog = post_create.objects.all().order_by('-id')
    cat = blog_category.objects.all()

    return render(request, "post.html", {"blogs": all_blog,"topblog":top_blog,'cat':cat})


def category(request,cat):
    if request.method == "POST":
        name = request.POST['name']
        contact = request.POST['contact']
        email = request.POST['email']
        message = request.POST['message']

        mes = f'''
    codeAjay.in

    Name : {name}
    Contact : {contact}
    Email : {email}
    Message : {message}
    '''

        print(mes)
        asyncio.run(send_telegram_message(mes))
        print("send !!")

    filtered_posts = post_create.objects.filter(category__slug=cat).order_by('-id')
    cat = blog_category.objects.all()
    all_blog = post_create.objects.all().order_by('-id')
    return render(request, 'category.html',{'tblog': filtered_posts,'cat':cat,"blogs": all_blog})