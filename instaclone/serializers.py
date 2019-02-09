from django.contrib.auth.models import User
from .models import Photo
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8)



    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class PhotoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username') #Associate Owner

    class Meta:
        model = Photo
        fields = ('id','post', 'image_file', 'image_url', 'owner', 'tags')














