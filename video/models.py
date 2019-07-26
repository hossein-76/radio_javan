from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.


class VideoCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'name:{self.name}, id:{self.id}'


class VideoManager(models.Manager):
    def approved_videos(self):
        return self.filter(approval_status="approved")

    def exclusive_videos(self):
        return self.filter(approval_status="approved", is_exclusive=True)


class Video(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        'art.Artist', on_delete=models.SET_NULL, null=True, blank=True)
    released_date = models.DateField()
    video_file = models.FileField()
    uploaded_date = models.DateTimeField(auto_now_add=True)
    is_exclusive = models.BooleanField(default=False)
    social_medias = JSONField(default=dict)
    tags = models.ManyToManyField('tag.Tag', blank=True)
    approval_status = models.CharField(max_length=50, choices=(
        ("approved", "approved"), ("pending", "pending"), ("rejected", "rejected")), default="pending")
    objects = VideoManager()

    def __str__(self):
        return f'id:{self.id}, name:{self.name}'


class VideoView(models.Model):
    datetime = models.DateField()
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self):
        return f'user:{self.user.id}, video:{self.video.id}'
