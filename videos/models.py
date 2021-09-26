from django.db import models

# Create your models here.
class Video(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=False, blank=False)
    video_type = models.CharField(max_length=255, null=False, blank=False)
    course = models.CharField(max_length=255, null=False, blank=False)
    url = models.URLField(max_length=1000, null=False, blank=False)
    video_number = models.IntegerField()
    transcription = models.JSONField(default=dict)