from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=254, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)


class uploaded_video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    title = models.CharField(max_length=100)
    uv = models.FileField(upload_to='uploaded_videos/')


    def __str__(self):
        return self.title
    

class tanslated_video(models.Model):
    uv = models.ForeignKey(uploaded_video, on_delete=models.CASCADE, default='')
    tv = models.FileField(upload_to='translated_videos/')
    
    def __str__(self):
        return self.uv
    

# class english_transcript(models.Model):
#     et_id = models.AutoField(primary_key=True)
#     uv_id = models.ForeignKey(uploaded_video, on_delete=models.CASCADE, default='')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     file = models.FileField(upload_to='english_transcripts/')
    
#     def __str__(self):
#         return self.et_id
    


# class chatbot_conversation(models.Model):
#     cc_id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     uv_id = models.ForeignKey(uploaded_video, on_delete=models.CASCADE)
#     et_id = models.ForeignKey(english_transcript, on_delete=models.CASCADE)
#     # cc_lang = models.CharField(max_length=100, default='')
#     file = models.FileField(upload_to='chatbot_conversation/')
    
#     def __str__(self):
#         return self.cc_id

# class chatbot_response(models.Model):
#     cr_id = models.AutoField(primary_key=True)
#     cc_id = models.ForeignKey(chatbot_conversation, on_delete=models.CASCADE)
#     # user = models.ForeignKey(User, on_delete=models.CASCADE)
#     # cr_lang = models.CharField(max_length=100, default='')
#     file = models.FileField(upload_to='chatbot_response/')
    
#     def __str__(self):
#         return self.cr_id

