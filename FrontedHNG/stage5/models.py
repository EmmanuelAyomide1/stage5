from django.db import models

# Create your models here.
class Video(models.Model):
    video=models.FileField(upload_to='videos/')
    transcript=models.TextField(blank=True, null=True)
    duration=models.CharField(max_length=10,blank=True, null=True)