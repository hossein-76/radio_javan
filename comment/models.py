from django.db import models

# Create your models here.


class CommentManager(models.Manager):
    def valid_comments(self):
        return self.filter(approval_status="approved", is_deleted=False)


class SongComment(models.Model):
    title = models.CharField(max_length=255)
    comment_text = models.TextField()
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)
    approval_status = models.CharField(max_length=50, choices=(
        ("approved", "approved"), ("pending", "pending"), ("rejected", "rejected")), default="pending")
    is_deleted = models.BooleanField(default=False)
    song = models.ForeignKey('music.Song', on_delete=models.CASCADE)
    objects = CommentManager()

    def __str__(self):
        return f'id:{self.id}, title:{self.title}'


class PodCastComment(models.Model):
    title = models.CharField(max_length=255)
    comment_text = models.TextField()
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)
    approval_status = models.CharField(max_length=50, choices=(
        ("approved", "approved"), ("pending", "pending"), ("rejected", "rejected")), default="pending")
    is_deleted = models.BooleanField(default=False)
    podcast = models.ForeignKey('podcast.PodCast', on_delete=models.CASCADE)
    objects = CommentManager()

    def __str__(self):
        return f'id:{self.id}, title:{self.title}'


class VideoComment(models.Model):
    title = models.CharField(max_length=255)
    comment_text = models.TextField()
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)
    approval_status = models.CharField(max_length=50, choices=(
        ("approved", "approved"), ("pending", "pending"), ("rejected", "rejected")), default="pending")
    is_deleted = models.BooleanField(default=False)
    video = models.ForeignKey('video.Video', on_delete=models.CASCADE)
    objects = CommentManager()

    def __str__(self):
        return f'id:{self.id}, title:{self.title}'

    