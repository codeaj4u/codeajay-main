from rest_framework import serializers
from .models import CustomUser,post_create,Comments

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'phone_number']
        extra_kwargs = {'password': {'write_only': True}}
    

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = post_create
        fields = '__all__'



# post comments


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'