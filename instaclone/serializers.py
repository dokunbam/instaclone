from django.contrib.auth.models import User
from .models import Photo
from rest_framework import serializers

class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ('id','post', 'image_file', 'image_url', 'owner', 'tags')