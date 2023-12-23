from django.shortcuts import render
from projects.models import Project
from api.models import post_create,blog_category
import asyncio
from telegram import Bot


async def send_telegram_message(message,image_path="null",teligram_token='6365955881:AAH-BYuMTer0UzmIJNbY04kI4awKHrm7maU',chat_id='6747562361'):
    try:
        bot = Bot(token=teligram_token)
        chat_id =chat_id
        message_text = message
        await bot.send_message(chat_id=chat_id, text=message_text)

        if image_path == "null":
            pass
        else:
            with open(image_path, 'rb') as photo:
                await bot.send_photo(chat_id=chat_id, photo=photo)
    except:
        print("message is not sent")



def home(request):

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


    all_blog = post_create.objects.all().order_by('-id')
    three_blog = post_create.objects.all().order_by('-id')[:3]
    cat = blog_category.objects.all()
    return render(request, 'index.html',{"blogs":all_blog,'tblog':three_blog,'cat':cat})




def contact(request):
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



    cat = blog_category.objects.all()
    all_blog = post_create.objects.all().order_by('-id')
    return render(request, 'contact.html',{"blogs":all_blog,'cat':cat})

def about(request):
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


    cat = blog_category.objects.all()
    all_blog = post_create.objects.all().order_by('-id')
    return render(request, 'about.html' ,{"blogs":all_blog,'cat':cat})

def privacy_policy(request):
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


    cat = blog_category.objects.all()
    all_blog = post_create.objects.all().order_by('-id')
    return render(request, 'privacy-policy.html',{"blogs":all_blog,'cat':cat})

