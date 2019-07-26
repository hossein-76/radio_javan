# Generated by Django 2.1 on 2019-07-26 14:58

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('art', '0001_initial'),
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PodCast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('released_date', models.DateField()),
                ('uploaded_date', models.DateTimeField(auto_now_add=True)),
                ('podcast_file', models.FileField(upload_to='')),
                ('is_exclusive', models.BooleanField(default=False)),
                ('social_medias', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('approval_status', models.CharField(choices=[('approved', 'approved'), ('pending', 'pending'), ('rejected', 'rejected')], default='pending', max_length=50)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='art.Artist')),
                ('tags', models.ManyToManyField(blank=True, to='tag.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='PodCastCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PodCastView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateField()),
                ('podcast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='podcast.PodCast')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
