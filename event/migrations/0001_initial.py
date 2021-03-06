# Generated by Django 2.1 on 2019-07-26 14:58

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('art', '0001_initial'),
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateTimeField()),
                ('lat', models.CharField(blank=True, max_length=255, null=True)),
                ('lng', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.TextField()),
                ('social_medias', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('price', models.FloatField()),
                ('approval_status', models.CharField(choices=[('approved', 'approved'), ('pending', 'pending'), ('rejected', 'rejected')], default='pending', max_length=50)),
                ('artist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='art.Artist')),
                ('tags', models.ManyToManyField(blank=True, to='tag.Tag')),
            ],
        ),
    ]
