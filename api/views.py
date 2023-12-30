from rest_framework import status
from django.contrib.auth import authenticate, login
from .serializers import UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout
from .models import CustomUser
from rest_framework import viewsets
from .models import post_create
from .serializers import PostCreateSerializer
from telegram import Bot
from rest_framework.decorators import api_view
from rest_framework.response import Response
import asyncio

from rest_framework import generics
from .models import Comments
from .serializers import CommentsSerializer


@api_view(['POST'])
def user_login(request):
    username_or_email_or_phone = request.data.get('username_or_email_or_phone')
    password = request.data.get('password')

    # Authenticate user by username, email, or phone number
    user = authenticate(request, username=username_or_email_or_phone, password=password)
    if not user:
        user = authenticate(request, email=username_or_email_or_phone, password=password)
    if not user:
        user = CustomUser.objects.filter(phone_number=username_or_email_or_phone).first()
        if user:
            user = authenticate(request, username=user.username, password=password)

    if user:
        login(request, user)
        return Response({'message': 'Logged in successfully'})
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)





@api_view(['POST'])
def user_registration(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
@permission_classes([IsAuthenticated]) 
def user_logout(request):
    logout(request)
    return Response({'message': 'Logged out successfully'})





class PostCreateViewSet(viewsets.ModelViewSet):
    queryset = post_create.objects.all()
    serializer_class = PostCreateSerializer




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




@api_view(['POST'])
def send_telegram_api(request):

    message = request.data.get('message')  # Get 'message' from request data
    image_path = request.data.get('image_path', "null")  # Get 'image_path' from request data or default to "null"

    try:
        asyncio.run(send_telegram_message(message,image_path=image_path))
        return Response({'status': 'success', 'message': 'Telegram message sent'})
    except:
        return Response({'status': 'error', 'message': 'Failed to send Telegram message'})


# API endpoint to list all comments or create a new comment
class CommentsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

# API endpoint to retrieve, update or delete a specific comment
class CommentsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class CommentsFilterByCategoryAPIView(generics.ListAPIView):
    serializer_class = CommentsSerializer

    def get_queryset(self):
        blog_category_id = self.kwargs['blog_category_id']
        return Comments.objects.filter(blog_category=blog_category_id)



