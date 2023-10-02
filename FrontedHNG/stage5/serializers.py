from .models import Video
from rest_framework import serializers


class VideoSerialize(serializers.ModelSerializer):
    class Meta:
        model=Video
        fields='__all__'
    def validate(self, data):
        if not data:
            print("no video uploaded")
            raise serializers.ValidationError("There's no uploaded video file")
        return data