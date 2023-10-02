from django.db import models

class VideoChunk(models.Model):
    session_id = models.CharField(max_length=100)
    chunk_number = models.IntegerField()
    total_chunks = models.IntegerField()
    video_chunk = models.FileField(upload_to='video_chunks/')

class Video(models.Model):
    session_id = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='complete_videos/')