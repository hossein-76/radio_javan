from django.db import models

# Create your models here.


class Advertisement(models.Model):
    title = models.CharFields(max_length=255)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    amount = models.IntegerField()
    type = models.CharField(max_length=255, choices=(
        ("video", "video"), ("sound", "sound"), ("banner", "banner")))
    ad_file = models.FileField()

    def __str__(self):
        return f'id:{self.id}, title:{self.title}'
