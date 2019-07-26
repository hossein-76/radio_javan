from django.db import models
from django.contrib.postgres.fields import JSONField


class Concert(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    artist = models.ForeignKey(
        'art.Artist', on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField()
    lat = models.CharField(max_length=255, null=True, blank=True)
    lng = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField()
    social_medias = JSONField(default=dict)
    price = models.FloatField()
    tags = models.ManyToManyField('tag.Tag', blank=True)
    approval_status = models.CharField(max_length=50, choices=(
        ("approved", "approved"), ("pending", "pending"), ("rejected", "rejected")), default="pending")

    def __str__(self):
        return f'id:{self.id}, name:{self.name}'
