from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.


class PodCastCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'name:{self.name}, id:{self.id}'


class PodCastManager(models.Manager):
    def approved_podcasts(self):
        return self.filter(approval_status="approved")

    def exclusive_podcasts(self):
        return self.filter(approval_status="approved", is_exclusive=True)


class PodCast(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        'art.Artist', on_delete=models.SET_NULL, null=True, blank=True)
    released_date = models.DateField()
    uploaded_date = models.DateTimeField(auto_now_add=True)
    podcast_file = models.FileField()
    is_exclusive = models.BooleanField(default=False)
    social_medias = JSONField(default=dict)
    tags = models.ManyToManyField('tag.Tag', blank=True)
    approval_status = models.CharField(max_length=50, choices=(
        ("approved", "approved"), ("pending", "pending"), ("rejected", "rejected")), default="pending")
    objects = PodCastManager()

    def __str__(self):
        return f'id:{self.id}, name:{self.name}'


class PodCastView(models.Model):
    datetime = models.DateField()
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)
    podcast = models.ForeignKey(PodCast, on_delete=models.CASCADE)

    def __str__(self):
        return f'user:{self.user.id}, podcast:{self.podcast.id}'
