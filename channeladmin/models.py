from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class VideoUpload(models.Model):
    caption = models.CharField(max_length=200)
    video =   models.FileField(upload_to='videos_uploaded',null=True,
                validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    date_uploaded = models.DateField()

    def  __str__(self):
        return  self.caption