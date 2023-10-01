from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Video
from .serializers import VideoSerialize
from django.core.files.storage import default_storage
from moviepy.editor import VideoFileClip
from rest_framework.parsers import MultiPartParser , FormParser
import speech_recognition as sr
import  os
from django.shortcuts import get_object_or_404
from django.http import FileResponse

# Create your views here.
class VideoPost(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        print(request.FILES.get('video'))
        vid=request.FILES.get('video')
        serialize_vid=VideoSerialize(data={'video':vid})
        if serialize_vid.is_valid(raise_exception=True):
            vid_instance=serialize_vid.save()
            raw_video=vid_instance.video
            vid_file_path = default_storage.save('tmp/' + raw_video.name, raw_video)
            absolute_path = default_storage.path(vid_file_path)
            vid=VideoFileClip(absolute_path)
            duration = vid.duration
            audio_file_path =default_storage.save('tmp/' + raw_video.name.split('.')[0] + '.wav',raw_video)
            absolute_path_aud=default_storage.path(audio_file_path)
            vid.audio.write_audiofile(absolute_path_aud,codec="pcm_s16le")
            recognizer=sr.Recognizer()
            with sr.AudioFile(absolute_path_aud) as source:
               audio_data=recognizer.record(source)
               try:
                    transcription=recognizer.recognize_google(audio_data)
               except sr.UnknownValueError:
                   transcription=""
            vid_instance.transcript=transcription
            vid_instance.duration=duration
            vid_instance.save()
            video_id=vid_instance.id
            return Response({"message":"created sucesfully","video_id":video_id},status=status.HTTP_201_CREATED)
    def get(self,request,video_id,*args,**kwargs):
        vedeo=get_object_or_404(Video,id=video_id)
        video_path=vedeo.video.path
        if os.path.exists(video_path):
                f=open(video_path,'rb')
                response=FileResponse(f)
                response['Content-Type']= 'video/mp4'
                return response
        return Response({"message":"Video not found"},status=status.HTTP_404_NOT_FOUND)
class TransGet(APIView):
    def get(self,request,video_id,*args,**kwargs):
        vedeo=get_object_or_404(Video,id=video_id)
        return Response({"transcript":vedeo.transcript,"duration":vedeo.duration},status=status.HTTP_200_OK)