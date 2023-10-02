from rest_framework import serializers
from .models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Mate:
        model = Video
        filde = '__all__'